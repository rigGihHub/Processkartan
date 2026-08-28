-- Maplini v0.8.0 Workspaces
create table if not exists public.workspaces (
  id text primary key,
  name text not null,
  owner_id uuid not null references auth.users(id) on delete cascade,
  created_at timestamptz not null default now()
);

create table if not exists public.workspace_members (
  workspace_id text not null references public.workspaces(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  role text not null check (role in ('owner','editor','viewer')),
  created_at timestamptz not null default now(),
  primary key (workspace_id,user_id)
);

alter table public.workspaces enable row level security;
alter table public.workspace_members enable row level security;
alter table public.processes add column if not exists workspace_id text references public.workspaces(id) on delete cascade;

create policy "workspace members read workspaces" on public.workspaces for select to authenticated
using (owner_id=auth.uid() or exists(select 1 from public.workspace_members wm where wm.workspace_id=id and wm.user_id=auth.uid()));

create policy "owners create workspaces" on public.workspaces for insert to authenticated
with check (owner_id=auth.uid());

create policy "members read memberships" on public.workspace_members for select to authenticated
using (user_id=auth.uid() or exists(select 1 from public.workspaces w where w.id=workspace_id and w.owner_id=auth.uid()));

create policy "owners manage memberships" on public.workspace_members for all to authenticated
using (exists(select 1 from public.workspaces w where w.id=workspace_id and w.owner_id=auth.uid()))
with check (exists(select 1 from public.workspaces w where w.id=workspace_id and w.owner_id=auth.uid()));

create policy "workspace users read processes" on public.processes for select to authenticated
using (
  (workspace_id is null and owner_id=auth.uid()) or
  (workspace_id is not null and exists(select 1 from public.workspace_members wm where wm.workspace_id=processes.workspace_id and wm.user_id=auth.uid()))
);

create policy "workspace editors insert processes" on public.processes for insert to authenticated
with check (
  (workspace_id is null and owner_id=auth.uid()) or
  (workspace_id is not null and exists(select 1 from public.workspace_members wm where wm.workspace_id=processes.workspace_id and wm.user_id=auth.uid() and wm.role in ('owner','editor')))
);

create policy "workspace editors update processes" on public.processes for update to authenticated
using (
  (workspace_id is null and owner_id=auth.uid()) or
  (workspace_id is not null and exists(select 1 from public.workspace_members wm where wm.workspace_id=processes.workspace_id and wm.user_id=auth.uid() and wm.role in ('owner','editor')))
)
with check (
  (workspace_id is null and owner_id=auth.uid()) or
  (workspace_id is not null and exists(select 1 from public.workspace_members wm where wm.workspace_id=processes.workspace_id and wm.user_id=auth.uid() and wm.role in ('owner','editor')))
);

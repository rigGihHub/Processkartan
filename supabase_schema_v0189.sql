-- Maplini v0.18.9 – cloud walkthrough history
-- Run after supabase_schema_v080.sql and supabase_schema_v0147.sql.

begin;

create table if not exists public.walkthrough_runs (
  id text primary key,
  process_id text not null references public.processes(id) on delete cascade,
  workspace_id text references public.workspaces(id) on delete cascade,
  process_owner_id uuid not null references auth.users(id) on delete cascade,
  created_by uuid not null references auth.users(id) on delete cascade,
  person text not null,
  started_at timestamptz not null,
  completed_at timestamptz not null,
  follow_up_status text not null default 'passed'
    check (follow_up_status in ('passed','open','resolved')),
  result jsonb not null default '{}'::jsonb,
  history jsonb not null default '[]'::jsonb,
  follow_up_updated_at timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

alter table public.walkthrough_runs enable row level security;

create index if not exists idx_walkthrough_runs_process_completed
  on public.walkthrough_runs(process_id, completed_at desc);
create index if not exists idx_walkthrough_runs_workspace_completed
  on public.walkthrough_runs(workspace_id, completed_at desc);
create index if not exists idx_walkthrough_runs_creator_completed
  on public.walkthrough_runs(created_by, completed_at desc);

drop policy if exists "walkthrough members read" on public.walkthrough_runs;
create policy "walkthrough members read" on public.walkthrough_runs
for select to authenticated
using (
  (workspace_id is null and process_owner_id=auth.uid())
  or
  (
    workspace_id is not null
    and exists(
      select 1 from public.workspace_members wm
      where wm.workspace_id=walkthrough_runs.workspace_id
        and wm.user_id=auth.uid()
    )
  )
);

drop policy if exists "walkthrough users create" on public.walkthrough_runs;
create policy "walkthrough users create" on public.walkthrough_runs
for insert to authenticated
with check (
  created_by=auth.uid()
  and (
    (workspace_id is null and process_owner_id=auth.uid())
    or
    (
      workspace_id is not null
      and process_owner_id=(select w.owner_id from public.workspaces w where w.id=walkthrough_runs.workspace_id)
      and exists(
        select 1 from public.workspace_members wm
        where wm.workspace_id=walkthrough_runs.workspace_id
          and wm.user_id=auth.uid()
      )
    )
  )
);

drop policy if exists "walkthrough followup update" on public.walkthrough_runs;
create policy "walkthrough followup update" on public.walkthrough_runs
for update to authenticated
using (
  created_by=auth.uid()
  or process_owner_id=auth.uid()
  or (
    workspace_id is not null
    and exists(
      select 1 from public.workspace_members wm
      where wm.workspace_id=walkthrough_runs.workspace_id
        and wm.user_id=auth.uid()
        and wm.role in ('owner','editor')
    )
  )
)
with check (
  process_owner_id=(
    select p.owner_id from public.processes p
    where p.id=walkthrough_runs.process_id
  )
  and (
    created_by=auth.uid()
    or process_owner_id=auth.uid()
    or (
      workspace_id is not null
      and exists(
        select 1 from public.workspace_members wm
        where wm.workspace_id=walkthrough_runs.workspace_id
          and wm.user_id=auth.uid()
          and wm.role in ('owner','editor')
      )
    )
  )
);

commit;

create table if not exists public.processes (
 id text primary key,
 owner_id uuid not null references auth.users(id) on delete cascade,
 name text not null,
 data jsonb not null default '{}'::jsonb,
 share_token text unique,
 share_mode text not null default 'private' check (share_mode in ('private','view')),
 created_at timestamptz not null default now(),
 updated_at timestamptz not null default now()
);
alter table public.processes enable row level security;
drop policy if exists "owner read" on public.processes;
create policy "owner read" on public.processes for select to authenticated using (auth.uid()=owner_id);
drop policy if exists "owner insert" on public.processes;
create policy "owner insert" on public.processes for insert to authenticated with check (auth.uid()=owner_id);
drop policy if exists "owner update" on public.processes;
create policy "owner update" on public.processes for update to authenticated using (auth.uid()=owner_id) with check (auth.uid()=owner_id);
drop policy if exists "owner delete" on public.processes;
create policy "owner delete" on public.processes for delete to authenticated using (auth.uid()=owner_id);
drop policy if exists "public shared view" on public.processes;
create policy "public shared view" on public.processes for select to anon using (share_mode='view' and share_token is not null);
create index if not exists idx_process_owner_updated on public.processes(owner_id,updated_at desc);
create index if not exists idx_process_share_token on public.processes(share_token);

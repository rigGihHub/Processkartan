-- Maplini v0.14.7 – workspace process ownership integrity
-- Run after supabase_schema_v080.sql.
-- Canonical rule: a process inside a workspace keeps the workspace owner's user id
-- in processes.owner_id. Editors may edit process content but may not claim ownership.

begin;

drop policy if exists "workspace editors insert processes" on public.processes;
drop policy if exists "workspace editors update processes" on public.processes;

create policy "workspace editors insert processes" on public.processes for insert to authenticated
with check (
  (workspace_id is null and owner_id=auth.uid()) or
  (
    workspace_id is not null
    and owner_id=(select w.owner_id from public.workspaces w where w.id=processes.workspace_id)
    and exists(
      select 1 from public.workspace_members wm
      where wm.workspace_id=processes.workspace_id
        and wm.user_id=auth.uid()
        and wm.role in ('owner','editor')
    )
  )
);

create policy "workspace editors update processes" on public.processes for update to authenticated
using (
  (workspace_id is null and owner_id=auth.uid()) or
  (
    workspace_id is not null
    and exists(
      select 1 from public.workspace_members wm
      where wm.workspace_id=processes.workspace_id
        and wm.user_id=auth.uid()
        and wm.role in ('owner','editor')
    )
  )
)
with check (
  (workspace_id is null and owner_id=auth.uid()) or
  (
    workspace_id is not null
    and owner_id=(select w.owner_id from public.workspaces w where w.id=processes.workspace_id)
    and exists(
      select 1 from public.workspace_members wm
      where wm.workspace_id=processes.workspace_id
        and wm.user_id=auth.uid()
        and wm.role in ('owner','editor')
    )
  )
);

commit;

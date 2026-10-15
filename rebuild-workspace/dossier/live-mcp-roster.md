# Live monday MCP tool roster

Source: the monday.com connector added in Claude Customize, as loaded into the user's Claude Code session on 2026-09-10 (its server id is not recorded here). These are the tool names only; each tool's schema has to be loaded before it can be called. Nothing has been live-tested yet.

## Tools (118)

activate-sequence, agent_catalog, all_api_read, all_api_write, all_monday_api, all_widgets_schema, board_insights, change_item_column_values, connect_external_agent, create-sequence, create-timeline-item, create-timeline-note, create_action, create_automation, create_board, create_column, create_dashboard, create_doc, create_folder, create_form, create_form_submission, create_group, create_item, create_items, create_notification, create_update, create_view, create_view_table, create_widget, create_workflow, create_workspace, deactivate-sequence, delete_action, delete_view, duplicate-sequence, enroll-item-in-sequence, execute_code, explore_meetings, finalize_asset_upload, form_questions_editor, get-activity-insights, get-board-sequences, get-contact-journey, get-custom-activities, get-sequence-analytics, get-timeline-items, get_action, get_asset_upload_url, get_assets, get_automation_runs, get_automation_statistics, get_board_activity, get_board_info, get_board_items_page, get_column_type_info, get_form, get_graphql_schema, get_meetings_content, get_monday_dev_sprints_boards, get_monday_knowledge, get_run_once_trigger_entities, get_sprint_summary, get_sprints_metadata, get_type_details, get_updates, get_user_context, get_workflow_run_once_status, invoke_process_planner, invoke_workflow_expert, list_actions, list_automations, list_users_and_teams, list_workspaces, manage_agent, manage_agent_knowledge, manage_agent_skills, manage_agent_triggers, manage_automations, move_object, publish_workflow, read_docs, run_action, run_workflow_once, search, search_meetings_content, show-assign, show-battery, show-chart, show-table, stop_workflow_run_once, submit_bug_or_feature_request, update_action, update_column, update_doc, update_folder, update_form, update_items, update_view, update_view_table, update_workspace, validate_workflow, vibe_ask, vibe_create, vibe_delete, vibe_get, vibe_list, vibe_publication, vibe_update, workspace_info

## Worth investigating first (names suggest capabilities the old plugin may not have had)
- manage_automations: may be able to deactivate or delete automations. The old plugin claimed automations were a one-way door.
- get_monday_knowledge: monday's own knowledge source. It could replace much of a static manual.
- invoke_process_planner, invoke_workflow_expert: monday-side AI planning helpers.
- all_api_read / all_api_write, alongside all_monday_api: raw GraphQL split into read and write.
- delete_view, move_object, update_folder, update_workspace: management operations.
- create_workflow, validate_workflow, publish_workflow, run_workflow_once: the monday workflows builder.
- get_assets, get_asset_upload_url, finalize_asset_upload: file and image upload, possibly for SOP diagrams in docs.
- Sequences, timeline and meetings tools (CRM and notetaker).
- vibe_* tools (monday vibe apps).
- show-chart, show-table, show-battery, show-assign: inline visual rendering.

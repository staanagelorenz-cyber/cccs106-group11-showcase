# ==============================================================================
# Camarines Sur Polytechnic Colleges - College of Computer Studies
# CCCS 106: Application Development and Emerging Technologies
# Laboratory Task: Collaborative DevTeam Showcase (Flet v0.86.5)
#
# Execution:
#   Desktop Window: flet run main.py
#   Hot-Reload Dev: flet run main.py -d
#   In-Browser Web: flet run --web main.py
# ==============================================================================

import sys
import flet as ft
from team_profiles import get_initial_team, build_profile_card, TeamMember


def main(page: ft.Page):
    # ==========================================================================
    # 1. APPLICATION WINDOW CONFIGURATION (Flet v0.86.5 API)
    # ==========================================================================
    page.title = "CCCS 106 - DevTeam Showcase & Collaboration Hub"
    page.window.width = 600
    page.window.height = 740
    page.window.resizable = False
    page.window.alignment = ft.Alignment.CENTER
    if not page.web:
        page.run_task(page.window.center)
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # ==========================================================================
    # 2. STATE VARIABLES (Shared Team State)
    # ==========================================================================
    base_prefix = getattr(sys, "base_prefix", sys.prefix)
    is_in_venv = sys.prefix != base_prefix or hasattr(sys, "real_prefix")
    tasks_completed_count = 0

    # ==========================================================================
    # 3. UI CONTROLS DEFINITION
    # ==========================================================================

    # --- Header Banner ---
    institution_header = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Icon(ft.Icons.GROUPS, size=32, color=ft.Colors.PRIMARY),
                    ft.Text(
                        "CCCS 106 DevTeam Hub",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PRIMARY,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text(
                "Camarines Sur Polytechnic Colleges - BSCS Application Development",
                size=11,
                color=ft.Colors.OUTLINE,
                text_align=ft.TextAlign.CENTER,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=4,
    )

    # Get Flet version dynamically
    try:
        import importlib.metadata
        flet_ver = importlib.metadata.version("flet")
    except Exception:
        flet_ver = getattr(getattr(ft, "version", None), "version", "0.86.5")

    # --- Environment Status Chip ---
    env_chip = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(
                    ft.Icons.VERIFIED_USER if is_in_venv else ft.Icons.WARNING_AMBER,
                    size=16,
                    color=ft.Colors.GREEN_700 if is_in_venv else ft.Colors.AMBER_800,
                ),
                ft.Text(
                    f"Env: {'ISOLATED (.venv)' if is_in_venv else 'GLOBAL PYTHON (Risk)'} | Flet v{flet_ver}",
                    size=11,
                    weight=ft.FontWeight.W_600,
                    color=ft.Colors.GREEN_900 if is_in_venv else ft.Colors.AMBER_900,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=6,
        ),
        padding=ft.Padding.symmetric(horizontal=12, vertical=6),
        bgcolor=ft.Colors.GREEN_50 if is_in_venv else ft.Colors.AMBER_50,
        border=ft.Border.all(
            1, ft.Colors.GREEN_200 if is_in_venv else ft.Colors.AMBER_200
        ),
        border_radius=20,
    )

    # --- Team Roster Container ---
    team_list = get_initial_team()
    team_cards_column = ft.Column(
        controls=[build_profile_card(member) for member in team_list],
        spacing=10,
    )

    # --- [DEVELOPER 2 & 3 COLLABORATIVE SECTION] ---
    # Sprint Task State & Goal Progress
    SPRINT_GOAL = 5

    # [Developer 2 Control]
    counter_label = ft.Text(
        "Sprint Tasks Completed: 0",
        size=14,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.PRIMARY,
    )

    # [Developer 3 Control]
    goal_status_badge = ft.Text(
        f"Status: In Progress (0/{SPRINT_GOAL} tasks)",
        size=12,
        color=ft.Colors.OUTLINE,
        weight=ft.FontWeight.W_500,
    )

    # [Developer 2 Control: Task Action Button]
    task_increment_btn = ft.Button(
        content="Complete Task (+1)",
        icon=ft.Icons.CHECK,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.PRIMARY,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    # ==========================================================================
    # 4. EVENT HANDLERS (Collaborative Logic Integration)
    # ==========================================================================
    def update_goal_progress():
        """Updates sprint goal progress badge and bounds controls (Developer 3 feature)."""
        if tasks_completed_count >= SPRINT_GOAL:
            goal_status_badge.value = f"Status: 🎉 SPRINT GOAL MET ({SPRINT_GOAL}/{SPRINT_GOAL})"
            goal_status_badge.color = ft.Colors.GREEN_700
            task_increment_btn.disabled = True
        else:
            goal_status_badge.value = f"Status: In Progress ({tasks_completed_count}/{SPRINT_GOAL} tasks)"
            goal_status_badge.color = ft.Colors.OUTLINE
            task_increment_btn.disabled = False

    # [Developer 2 Handler]
    def handle_increment_task(e):
        nonlocal tasks_completed_count
        # Boundary Constraint: strictly cap at SPRINT_GOAL (maximum 5)
        if tasks_completed_count < SPRINT_GOAL:
            tasks_completed_count += 1
            counter_label.value = f"Sprint Tasks Completed: {tasks_completed_count}"
            update_goal_progress()
            page.update()

    # [Developer 2 Handler]
    def handle_reset_counter(e):
        nonlocal tasks_completed_count
        tasks_completed_count = 0
        counter_label.value = f"Sprint Tasks Completed: {tasks_completed_count}"
        update_goal_progress()
        page.update()

    task_increment_btn.on_click = handle_increment_task

    # [Developer 3 Handler]
    def handle_theme_toggle(e):
        if theme_switch.value:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    theme_switch = ft.Switch(
        label="Dark Mode",
        value=False,
        on_change=handle_theme_toggle,
    )

    # --- Controls Action Row ---
    action_controls_row = ft.Row(
        controls=[
            task_increment_btn,
            ft.IconButton(
                icon=ft.Icons.REFRESH,
                tooltip="Reset Counter",
                icon_color=ft.Colors.GREY_600,
                on_click=handle_reset_counter,
            ),
            theme_switch,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # ==========================================================================
    # 5. ASSEMBLE PAGE CONTROL TREE
    # ==========================================================================
    page.add(
        ft.Column(
            controls=[
                institution_header,
                ft.Container(height=4),
                env_chip,
                ft.Divider(height=16),
                ft.Row(
                    controls=[
                        ft.Text(
                            "COLLABORATIVE TEAM ROSTER",
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.PRIMARY,
                        ),
                        ft.Text(
                            f"{len(team_list)} Members",
                            size=11,
                            color=ft.Colors.OUTLINE,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                team_cards_column,
                ft.Divider(height=16),
                ft.Row(
                    controls=[counter_label, goal_status_badge],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                action_controls_row,
                ft.Divider(height=16),
                ft.Text(
                    "CCCS 106: Week 2 Laboratory Exercise • Git Collaboration Workflow",
                    size=10,
                    color=ft.Colors.GREY_500,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
    )


# ==============================================================================
# 6. APPLICATION RUNNER
# ==============================================================================
if __name__ == "__main__":
    if hasattr(ft, "run"):
        ft.run(main, assets_dir="assets")
    else:
        ft.app(target=main, assets_dir="assets")

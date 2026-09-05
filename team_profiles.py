# ==============================================================================
# Camarines Sur Polytechnic Colleges - College of Computer Studies
# CCCS 106: Application Development and Emerging Technologies
# Module: team_profiles.py - Team Data Model & Flet UI Component Builders
# ==============================================================================

from dataclasses import dataclass
from typing import List, Optional
import flet as ft


@dataclass
class TeamMember:
    """Represents a member of the software development team."""

    student_id: str
    full_name: str
    role: str
    specialization: str
    github_handle: str
    avatar_icon: ft.IconData = ft.Icons.ACCOUNT_CIRCLE
    accent_color: str = ft.Colors.BLUE_700
    photo_url: Optional[str] = None  # URL (e.g. GitHub avatar) or local path to student's photo


# ==============================================================================
# BASELINE REPOSITORY DATA (Initial Project Setup)
# ==============================================================================
def get_initial_team() -> List[TeamMember]:
    """Returns the baseline team roster.

    STUDENT COLLABORATION INSTRUCTIONS (3-MEMBER TEAMS):
    - Developer 1: Update your profile details in the DEV 1 SECTION (Branch: feature/dev1-profile)
    - Developer 2: Update your profile details in the DEV 2 SECTION (Branch: feature/dev2-state)
    - Developer 3: Update your profile details in the DEV 3 SECTION (Branch: feature/dev3-features)
    """
    members = [
        # ----------------------------------------------------------------------
        # TODO: [DEVELOPER 1 TASK] - Branch: feature/dev1-profile
        # Replace Developer 1 profile with your real student details:
        # (Add your photo URL e.g. "https://github.com/<username>.png" or local path)
        # ----------------------------------------------------------------------
        TeamMember(
            student_id="2411288",
            full_name="Gelorenz D. Sta. Ana",
            role="Lead Frontend UI Developer",
            specialization="Flet Reactive Widgets & Material 3 Layouts",
            github_handle="@staanagelorenz-cyber",
            avatar_icon=ft.Icons.PALETTE,
            accent_color=ft.Colors.TEAL_700,
            photo_url="/dev1.jpg",                 # Photo: local asset or URL (e.g. "https://github.com/dev1-github.png")
        ),
        # ----------------------------------------------------------------------
        # TODO: [DEVELOPER 2 TASK] - Branch: feature/dev2-state
        # Replace Developer 2 profile with your real student details:
        # ----------------------------------------------------------------------
        TeamMember(
            student_id="2411282",  # example: "2024-10456"
            full_name="Renz Angelo S. Priela", # example: "Juan Dela Cruz"
            role="Backend & State Engineer",
            specialization="State Mutation & Event Handlers",
            github_handle="@rnxee",          # example: "@jdelacruz-cspc"
            avatar_icon=ft.Icons.DATA_OBJECT,
            accent_color=ft.Colors.AMBER_800,
            photo_url="/dev2.jpg",                 # Photo: local asset or URL (e.g. "https://github.com/dev2-github.png")
        ),
        # ----------------------------------------------------------------------
        # TODO: [DEVELOPER 3 TASK] - Branch: feature/dev3-features
        # Replace Developer 3 profile with your real student details:
        # ----------------------------------------------------------------------
        TeamMember(
            student_id="[Dev 3] Student ID Here",  # example: "2024-10789"
            full_name="[Dev 3] Student Name Here", # example: "Angelo Reyes"
            role="QA & Feature Engineer",
            specialization="Testing Diagnostics, Theme Engine & Controls",
            github_handle="@dev3-github",          # example: "@areyes-cspc"
            avatar_icon=ft.Icons.BUG_REPORT,
            accent_color=ft.Colors.INDIGO_700,
            photo_url="/dev3.jpg",                 # Photo: local asset or URL (e.g. "https://github.com/dev3-github.png")
        ),
    ]
    return members


# ==============================================================================
# FLET REUSABLE UI COMPONENT BUILDER (Material 3 Card)
# ==============================================================================
def build_profile_card(member: TeamMember) -> ft.Container:
    """Builds a responsive, styled Material 3 profile card for a team member."""
    if member.photo_url:
        avatar_control = ft.Container(
            content=ft.Image(
                src=member.photo_url,
                width=52,
                height=52,
                fit=ft.BoxFit.COVER,
                border_radius=26,
                error_content=ft.Container(
                    content=ft.Icon(member.avatar_icon, size=26, color=member.accent_color),
                    alignment=ft.Alignment.CENTER,
                ),
            ),
            width=52,
            height=52,
            border_radius=26,
            border=ft.Border.all(2, member.accent_color),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=4,
                color=ft.Colors.BLACK_12,
                offset=ft.Offset(0, 1),
            ),
            tooltip=f"{member.full_name}'s Photo",
        )
    else:
        avatar_control = ft.Container(
            content=ft.Icon(
                member.avatar_icon,
                size=26,
                color=member.accent_color,
            ),
            width=52,
            height=52,
            alignment=ft.Alignment.CENTER,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            border_radius=26,
            border=ft.Border.all(2, ft.Colors.OUTLINE_VARIANT),
            tooltip=f"Placeholder for {member.full_name} (Set photo_url to display photo)",
        )

    return ft.Container(
        content=ft.Row(
            controls=[
                avatar_control,
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(
                                    member.full_name,
                                    size=15,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.ON_SURFACE,
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        member.student_id,
                                        size=10,
                                        weight=ft.FontWeight.W_600,
                                        color=member.accent_color,
                                    ),
                                    padding=ft.Padding.symmetric(horizontal=6, vertical=2),
                                    border=ft.Border.all(1, member.accent_color),
                                    border_radius=6,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Text(
                            f"Role: {member.role}",
                            size=12,
                            weight=ft.FontWeight.W_500,
                            color=ft.Colors.PRIMARY,
                        ),
                        ft.Text(
                            f"Focus: {member.specialization}",
                            size=11,
                            color=ft.Colors.OUTLINE,
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.CODE, size=14, color=ft.Colors.GREY_600),
                                ft.Text(
                                    member.github_handle,
                                    size=11,
                                    color=ft.Colors.GREY_600,
                                    font_family="monospace",
                                ),
                            ],
                            spacing=4,
                        ),
                    ],
                    spacing=2,
                    expand=True,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=14,
        ),
        padding=14,
        border_radius=14,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGH,
        border=ft.Border.all(1, ft.Colors.OUTLINE_VARIANT),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=6,
            color=ft.Colors.BLACK_12,
            offset=ft.Offset(0, 2),
        ),
    )

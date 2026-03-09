"""
SkillForge CLI — Build. Test. Sign. Ship.
ESLint + Jest for AI Agent Skills across OpenClaw, Claude Code, Cursor, Windsurf.
"""

import typer
from rich.console import Console
from rich.panel import Panel

from toolmark.commands.bench import bench_command
from toolmark.commands.compat import compat_command
from toolmark.commands.init import init_command
from toolmark.commands.publish import publish_command
from toolmark.commands.scan import scan_command
from toolmark.commands.test import test_command

app = typer.Typer(
    name="toolmark",
    help="Build, test, and publish AI agent skills across every platform.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    pretty_exceptions_enable=False,
)

console = Console()

BANNER = """
[bold red]ToolMark[/] [dim]v0.1.0[/]
[dim]Build. Test. Sign. Ship — Across Every Agent Platform.[/]
"""


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        console.print(Panel(BANNER, border_style="dim red", padding=(0, 2)))


# Register subcommands
app.command("init", help="Scaffold a new skill project")(init_command)
app.command("test", help="Run LLM-as-judge evaluation on your skill")(test_command)
app.command("scan", help="Run security scanner (prompt injection, exfiltration, etc.)")(
    scan_command
)
app.command("compat", help="Check cross-platform compatibility")(compat_command)
app.command("bench", help="Benchmark latency, tokens, and quality score")(bench_command)
app.command("publish", help="Publish to ClawHub, Claude Code, Cursor, Windsurf")(publish_command)


def entry():
    app()


if __name__ == "__main__":
    entry()

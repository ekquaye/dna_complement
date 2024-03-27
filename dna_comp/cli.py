"""Console script for dna_comp."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("python-dna_comp-package")
    click.echo("=" * len("python-dna_comp-package"))
    click.echo("Python package dna_comp with MPI Evolutionary Biology branding.")


if __name__ == "__main__":
    main()  # pragma: no cover

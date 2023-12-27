"""
Main cli or app entry point
"""
from my_lib.predict import predict, read_file, read_url
import click


@click.command("main")
@click.option("--path")
@click.option("--url")
def main(path, url):
    if path:
        text = read_file(path)
    elif url:
        text = read_url(url)

    summarised_text = predict(text)

    click.echo(click.style(summarised_text, fg="green"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()

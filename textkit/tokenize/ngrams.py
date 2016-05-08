import click
import nltk
from textkit.utils import output, read_tokens


@click.command('words2ngrams')
@click.argument('tokens', type=click.File('r'), default=click.open_file('-'))
@click.option('-s', '--sep', default=' ',
              help='Separator between words in bigram output.',
              show_default=True)
@click.option('-n', '--num', default=2,
              help='Length of the n-gram',
              show_default=True)
def words2ngrams(sep, num, tokens):
    '''Tokenize words into ngrams. ngrams are n-length word tokens.
    Punctuation is considered as a separate token.'''

    content = read_tokens(tokens)
    ngrams = list(nltk.ngrams(content, num))
    [output(sep.join(ngram)) for ngram in ngrams]

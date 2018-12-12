#!usr/bin/perl
use strict;
use warnings;
use v5.12;
use Getopt::Long;

my @files;
my %words;
my $output = "";
my $dir    = "";

GetOptions(
	'dir|d=s'    => \$dir,
	'output|o=s' => \$output,
	'help|h'     => \&help,
)
or die "Error parsing command-line arguments\n";

&help unless $dir and $output;

@files = <$dir*.txt>;
foreach my $file (@files) {
	open(FH,'<',$file) or next;
	print "[Reading $file ... ]\n";
	while(my $row = <FH>) {
		chomp $row;
		$row =~ s/[\.|\!|\?|\,|\(|\)|\"|\&]//g;
		next if $row =~ m/^\s*\[.*\]\s*$/;

		my @curr_words = split ' ',$row;

		foreach my $word (@curr_words) {
			$word =~ s/^\'//;
			$word = lc $word;
			if($words{$word}) {
				$words{$word}++;
			} else {
				$words{$word} = 1;
			}
		}
	}
}

open(FH,'>',$output) or die "Error while trying to write $output\n";
foreach my $word (sort keys %words) {
	print FH "$word,$words{$word}\n";
}
close(FH);

sub help {
	my $menu = "Usage:\n"
	          ."	read_lyrics.pl -d <dir> -o <file>\n"
						."	read_lyrics.pl [-h|--help]\n"
						."\n"
						."Options\n"
						."	--dir     -d      Directory to read through text files\n"
						."	--output  -o      Output file (CSV) with words and frequencies\n";

	print($menu);
	exit(0);
}

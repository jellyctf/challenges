# vlookup_hot_singles

looks like this is some kind of dating site for nerds?
weird, figure out who the admin is and access their panel

explicit hint: you'll have to put on the wig and become jelly by forging a JWT with the secret from the source

# vlookup_hot_singles 2
oh. it's her. well, see if you can get the flag at /app/flag.txt and then get out of there

tool hint: some of the libraries are at a specific version for a reason. try using something like https://github.com/aquasecurity/trivy to see if there's anything interesting worth exploiting
hint: not all files are parsed by lxml
explicit hint: CVE-2017-5992 XXE in `docProps/core.xml`. pocs exist on the internet
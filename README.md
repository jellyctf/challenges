# challenges

| name                         | category  | author      | diffic | on ctfd?  | tested? |
| ----                         | ----      | -------     | ---    | ---       | ---     |
| cult_classic_1               | crypto    | Sheepiroo   | easy   | ✅        | ❌     |
| cult_classic_2               | crypto    | Sheepiroo   | easy   | ✅        | ❌     |
| dizzy_fishman                | crypto    | Sheepiroo   | hard   | ✅        | ❌     |
| exclusively_yours            | crypto    | Sheepiroo   | med    | ✅        | ❌     |
| the_brewing_secrets          | crypto    | Sheepiroo   | hard   | ✅        | ❌     |
| rsain't                      | crypto    | Sheepiroo   | ?      | ❌        | ❌     |
| you're_based                 | crypto    | Sheepiroo   | easy   | ✅        | ❌     |
| you're_baba_based            | crypto    | Sheepiroo   | med    | ✅        | ❌     |
| alien_transmission           | forensics | Sheepiroo   | easy   | ✅        | ❌     |
| head_empty                   | forensics | arepi_nemui | med    | ✅        | ✅     |
| head_empty_2                 | forensics | arepi_nemui | hard   | ✅        | ✅     |
| mpreg                        | forensics | Sheepiroo   | med    | ✅        | ✅     |
| oshi_mark                    | forensics | 2ndmeow     | med    | ✅        | ❌     |
| the_REAL_truth               | forensics | arepi_nemui | med    | ✅        | ✅     |
| the_REAL_truth_2             | forensics | arepi_nemui | hard   | ✅        | ✅     |
| just_win_lol                 | misc      | arepi_nemui | hard   | ✅        | ✅     |
| this_is_canon                | misc      | Sheepiroo   | ?      | ❌        | ❌     |
| yapping                      | misc      | kuuhaku0989 | ?      | ❌        | ❌     |
| into_the_atmosphere          | osint     | arepi_nemui | easy   | ✅        | ✅     |
| secret_engineering_role_play | osint     | arepi_nemui | med    | ✅        | ✅     |
| stalknights_1                | osint     | Sheepiroo   | easy   | ✅        | ✅     |
| stalknights_2                | osint     | Sheepiroo   | med    | ✅        | ✅     |
| stalknights_3                | osint     | Sheepiroo   | med    | ✅        | ❌     |
| stalknights_4                | osint     | Sheepiroo   | hard   | ✅        | ✅     |
| stalknights_5                | osint     | Sheepiroo   | med    | ✅        | ✅     |
| super_fan                    | osint     | arepi_nemui | hard   | ✅        | ✅     |
| phase_coffee_1               | pwn       | Sheepiroo   | easy   | ✅        | ❌     |
| phase_coffee_2               | pwn       | Sheepiroo   | med    | ✅        | ❌     |
| phase_coffee_3               | pwn       | Sheepiroo   | med    | ✅        | ❌     |
| Awassmbely_1                 | rev       | lisp_beamer | ?      | ❌        | ❌     |
| lost_in_translation          | rev       | kuuhaku0989 | ?      | ❌        | ✅     |
| rev1                         | rev       | arepi_nemui | easy   | ✅        | ❌     |
| aidoru                       | web       | Sheepiroo   | easy   | ✅        | ✅     |
| awafy_me                     | web       | Sheepiroo   | easy   | ✅        | ✅     |
| awascii_validator            | web       | Sheepiroo   | med    | ✅        | ✅     |
| bro_visited_his_site         | web       | arepi_nemui | med    | ✅        | ✅     |
| bro_visited_his_site_2       | web       | arepi_nemui | med    | ✅        | ✅     |
| do_not_trust                 | web       | arepi_nemui | easy   | ✅        | ✅     |
| factory_clicker              | web       | lisp_beamer | easy   | ✅        | ✅     |
| pentest_on_stream            | web       | arepi_nemui | hard   | ✅        | ✅     |
| vlookup_hot_singles          | web       | arepi_nemui | easy   | ✅        | ✅     |
| vlookup_hot_singles_2        | web       | arepi_nemui | hard   | ✅        | ✅     |


## folder structure
* category
    - challenge name
        - dist - for files given to the user at the start of the challenge (e.g. source with flags redacted, binaries, etc.)
        - solve - solutions in either text format or a script
        - src - solution source


## site text
Welcome to JellyCTF! This is a beginner to intermediate targeted [jeopardy](https://ctftime.org/ctf-wtf/) style [CTF](https://en.wikipedia.org/wiki/Capture_the_flag_(cybersecurity)) themed around the Virtual YouTuber [Jelly Hoshiumi](https://www.youtube.com/@JellyHoshiumi), intended to introduce her ~~awatistic~~ audience into security challenges.

Challenges are split up into categories and dynamically scored, based on how many solves it has. The categories are:

1. Web
2. Crypto
3. Forensics
4. OSINT
5. Rev
6. Pwn
7. Misc

We recommend searching the internet for similar problems that may have CTF writeups in order to get an idea of how to solve problems. For challenges with source, try grepping for `jellyCTF{` to see where you want to get to and trace backwards.

The event will run from XXXX-YY-ZZ to XXXX-YY-ZZ, after which the challenges source code and solutions will be released. Feel free to post your own writeups after the event has ended, too.

### rules
1. Do not attack the scoreboard (the base jellyc.tf domain), the infrastructure in general, or other teams. If you are not sure about the scope of a challenge, please open a ticket on the [Discord](https://discord.gg/MDNfMuGsr4).
2. Do not bruteforce any remote challenges. They're designed to be solved without, and it causes unnecessary strain on the infrastructure.
3. Unless you're Jelly, do not share flags or solutions with other teams, but feel free to give hints in the interest of learning.
4. Unless otherwise specified, the flag format is standard ASCII characters wrapped in `jellyCTF{}`.

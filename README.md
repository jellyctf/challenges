# challenges

| name                         | category  | author      | points | complete? | tested? |
| ----                         | ----      | -------     | ---    | ---       | ---     |
| cult_classic                 | crypto    | Sheepiroo   | ?      | ❌        | ❌     |
| dizzy_fishman                | crypto    | Sheepiroo   | 2000   | ✅        | ❌     |
| exclusively_yours            | crypto    | Sheepiroo   | 500    | ✅        | ❌     |
| passcode_lock                | crypto    | Sheepiroo   | ?      | ❌        | ❌     |
| rsain't                      | crypto    | Sheepiroo   | ?      | ❌        | ❌     |
| alien_transmission           | forensics | Sheepiroo   | 500    | ✅        | ❌     |
| head_empty                   | forensics | arepi_nemui | 1000   | ✅        | ❌     |
| head_empty_2                 | forensics | arepi_nemui | 2000   | ✅        | ❌     |
| mpreg                        | forensics | Sheepiroo   | 1000   | ✅        | ❌     |
| oshi_mark                    | forensics | 2ndmeow     | ?      | ❌        | ❌     |
| the_REAL_truth               | forensics | arepi_nemui | 1500   | ✅        | ❌     |
| the_REAL_truth_2             | forensics | arepi_nemui | 2000   | ✅        | ❌     |
| just_win_lol                 | misc      | arepi_nemui | 2000   | ✅        | ❌     |
| this_is_canon                | misc      | Sheepiroo   | ?      | ❌        | ❌     |
| yapping                      | misc      | kuuhaku0989 | ?      | ❌        | ❌     |
| into_the_atmosphere          | osint     | arepi_nemui | 500    | ✅        | ❌     |
| secret_engineering_role_play | osint     | arepi_nemui | 1000   | ✅        | ❌     |
| stalknights_1                | osint     | Sheepiroo   | 1000   | ✅        | ❌     |
| stalknights_2                | osint     | Sheepiroo   | 2000   | ✅        | ❌     |
| stalknights_3                | osint     | Sheepiroo   | 2000   | ✅        | ❌     |
| stalknights_6                | osint     | Sheepiroo   | ?      | ❌        | ❌     |
| super_fan                    | osint     | arepi_nemui | 2000   | ✅        | ❌     |
| phase_coffee_1               | pwn       | Sheepiroo   | 500    | ✅        | ❌     |
| phase_coffee_2               | pwn       | Sheepiroo   | 1000   | ✅        | ❌     |
| phase_coffee_3               | pwn       | Sheepiroo   | 1000   | ✅        | ❌     |
| Awassmbely_1                 | rev       | lisp_beamer | ?      | ❌        | ❌     |
| lost_in_translation          | rev       | kuuhaku0989 | ?      | ❌        | ❌     |
| rev1                         | rev       | arepi_nemui | 500    | ✅        | ❌     |
| aidoru                       | web       | Sheepiroo   | ?      | ❌        | ❌     |
| awafy_me                     | web       | Sheepiroo   | ?      | ❌        | ❌     |
| awascii_validator            | web       | Sheepiroo   | ?      | ❌        | ❌     |
| bro_visited_his_site         | web       | arepi_nemui | 1000   | ✅        | ❌     |
| bro_visited_his_site_2       | web       | arepi_nemui | 1000   | ✅        | ❌     |
| factory_clicker              | web       | lisp_beamer | ?      | ❌        | ❌     |
| pentest_on_stream            | web       | arepi_nemui | 2000   | ✅        | ❌     |
| vlookup_hot_singles          | web       | arepi_nemui | 500    | ✅        | ❌     |
| vlookup_hot_singles_2        | web       | arepi_nemui | 2000   | ✅        | ❌     |


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
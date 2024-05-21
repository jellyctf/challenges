# challenges

| name                         | category  | author      | points | complete? |
| ----                         | ----      | -------     | ---    | ❌        | 
| cult_classic                 | crypto    | Sheepiroo   | ?      | ❌        | 
| dizzy_fishman                | crypto    | Sheepiroo   | ?      | ❌        | 
| exclusively_yours            | crypto    | Sheepiroo   | ?      | ❌        | 
| passcode_lock                | crypto    | Sheepiroo   | ?      | ❌        | 
| rsain't                      | crypto    | Sheepiroo   | ?      | ❌        | 
| alien_transmission           | forensics | Sheepiroo   | ?      | ❌        | 
| head_empty                   | forensics | arepi_nemui | ?      | ✅        | 
| head_empty_2                 | forensics | arepi_nemui | ?      | ✅        | 
| mpreg                        | forensics | Sheepiroo   | ?      | ❌        | 
| oshi_mark                    | forensics | 2ndmeow     | ?      | ❌        |
| the_REAL_truth               | forensics | arepi_nemui | ?      | ✅        | 
| the_REAL_truth_2             | forensics | arepi_nemui | ?      | ✅        | 
| just_win_lol                 | misc      | arepi_nemui | ?      | ✅        | 
| this_is_canon                | misc      | Sheepiroo   | ?      | ❌        | 
| yapping                      | misc      | kuuhaku0989 | ?      | ❌        | 
| into_the_atmosphere          | osint     | arepi_nemui | ?      | ✅        | 
| secret_engineering_role_play | osint     | arepi_nemui | ?      | ✅        | 
| stalknights_1                | osint     | Sheepiroo   | ?      | ❌        | 
| stalknights_2                | osint     | Sheepiroo   | ?      | ❌        | 
| stalknights_3                | osint     | Sheepiroo   | ?      | ❌        | 
| stalknights_6                | osint     | Sheepiroo   | ?      | ❌        | 
| super_fan                    | osint     | arepi_nemui | ?      | ✅        | 
| phase_coffee                 | pwn       | Sheepiroo   | ?      | ❌        | 
| phase_coffee_FINAL           | pwn       | Sheepiroo   | ?      | ❌        | 
| phase_coffee_FINAL_UPDATED   | pwn       | Sheepiroo   | ?      | ❌        | 
| lost_in_translation          | rev       | kuuhaku0989 | ?      | ❌        | 
| rev1                         | rev       | arepi_nemui | ?      | ✅        | 
| aidoru                       | web       | Sheepiroo   | ?      | ❌        | 
| awafy_me                     | web       | Sheepiroo   | ?      | ❌        | 
| awascii_validator            | web       | Sheepiroo   | ?      | ❌        | 
| bro_visited_his_site         | web       | arepi_nemui | ?      | ✅        | 
| bro_visited_his_site_2       | web       | arepi_nemui | ?      | ✅        | 
| pentest_on_stream            | web       | arepi_nemui | ?      | ✅        | 
| vlookup_hot_singles          | web       | arepi_nemui | ?      | ✅        | 


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
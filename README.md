![jellyctf-resize](https://github.com/user-attachments/assets/0a26e774-3942-4944-8d07-9559fd055f27)

Info
----

Welcome to jellyCTF! This is a beginner to intermediate targeted [jeopardy](https://ctftime.org/ctf-wtf/) style [CTF](https://en.wikipedia.org/wiki/Capture_the_flag_(cybersecurity)) themed around the Virtual YouTuber [Jelly Hoshiumi](https://www.youtube.com/@JellyHoshiumi), intended to introduce her awatistic awesome audience to security challenges.  

*   Challenges are split up into categories and dynamically scored based on how many solves they have, lowering in value the more people solve them, starting at 1000 points and going down to 100 after 200 solves.
*   The flag format is standard ASCII characters wrapped in `jellyCTF{}`, unless specified otherwise in the challenge description.
*   If you're unsure how to solve a challenge, we recommend:
    1.  Searching the internet for similar problems that may have CTF writeups in order to get an idea of how to solve problems.
    2.  For challenges with source, try grepping for `jellyCTF{` to see where you want to get to tracing the code path backwards.
    3.  Making use of the hints system for challenges that have them.
*   The event will run from {{ ctf\_start }} to {{ ctf\_end }}, after which the scoreboard will close and challenge source code and solutions will be released. The site and challenges will stay up until 2024-06-30T23:00:00Z (in ). Feel free to post your own writeups after the event has ended, too.
  

Rules
-----

1.  Do not attack the scoreboard (the base jellyc.tf domain), the infrastructure in general, or other teams. If you are not sure about the scope of a challenge, please open a ticket on the [Discord](https://discord.gg/MDNfMuGsr4).
2.  Do not bruteforce any remote challenges. They're designed to be solved without, and it causes unnecessary strain on the infrastructure.
3.  Do not attempt to exploit any challenges further after solving and obtaining the flag(s), including privilege escalation, defacing or DoS.
4.  Do not share flags or solutions with other teams (unless you're Jelly and streaming), but feel free to give hints in the interest of learning.
5.  Do not be a troglodyte.

Sample flag: jellyCTF{L1k3\_th15}

  

Resources
---------

*   [https://github.com/TempTempai/AWA5.0/blob/6fe3b2ef290a3df9c94822634c4ceb6c872cd2fd/AWA5.0%20Specs.pdf](https://github.com/TempTempai/AWA5.0/blob/6fe3b2ef290a3df9c94822634c4ceb6c872cd2fd/AWA5.0%20Specs.pdf)
*   [https://book.hacktricks.xyz/](https://book.hacktricks.xyz/)
*   [https://portswigger.net/web-security/all-topics](https://portswigger.net/web-security/all-topics)
*   [https://cheatsheet.haax.fr/](https://cheatsheet.haax.fr/)
*   [https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/)
*   [https://ctf101.org/](https://ctf101.org/)
*   [https://ir0nstone.gitbook.io/notes](https://ir0nstone.gitbook.io/notes)
*   [https://www.ctfrecipes.com/](https://www.ctfrecipes.com/)

# challenges

| name                         | category  | author      | diffic | on ctfd?  | tested? |
| ----                         | ----      | -------     | ---    | ---       | ---     |
| cherry                       | crypto    | Meow Mix    | hard   | ✅        | ❌     |
| cipher_check                 | crypto    | Meow Mix    | easy   | ✅        | ✅     |
| cult_classic_1               | crypto    | Sheepiroo   | easy   | ✅        | ❌     |
| cult_classic_2               | crypto    | Sheepiroo   | easy   | ✅        | ❌     |
| dizzy_fishman                | crypto    | Sheepiroo   | hard   | ✅        | ❌     |
| exclusively_yours            | crypto    | Sheepiroo   | med    | ✅        | ✅     |
| the_brewing_secrets          | crypto    | Sheepiroo   | hard   | ✅        | ❌     |
| rsain't                      | crypto    | Sheepiroo   | ?      | ❌        | ❌     |
| you're_based                 | crypto    | Sheepiroo   | easy   | ✅        | ✅     |
| you're_baba_based            | crypto    | Sheepiroo   | med    | ✅        | ❌     |
| alien_transmission           | forensics | Sheepiroo   | easy   | ✅        | ✅     |
| head_empty                   | forensics | arepi_nemui | med    | ✅        | ✅     |
| head_empty_2                 | forensics | arepi_nemui | hard   | ✅        | ✅     |
| mpreg                        | forensics | Sheepiroo   | med    | ✅        | ✅     |
| oshi_mark                    | forensics | Meow Mix    | med    | ✅        | ✅     |
| the_REAL_truth               | forensics | arepi_nemui | med    | ✅        | ✅     |
| the_REAL_truth_2             | forensics | arepi_nemui | hard   | ✅        | ✅     |
| is_jelly_stuck               | misc      | Meow Mix    | easy   | ✅        | ✅     |
| just_win_lol                 | misc      | arepi_nemui | hard   | ✅        | ✅     |
| this_is_canon                | misc      | Sheepiroo   | ?      | ❌        | ❌     |
| yapping                      | misc      | kuuhaku0989 | ?      | ❌        | ❌     |
| into_the_atmosphere          | osint     | arepi_nemui | easy   | ✅        | ✅     |
| secret_engineering_role_play | osint     | arepi_nemui | med    | ✅        | ✅     |
| stalknights_1                | osint     | Sheepiroo   | easy   | ✅        | ✅     |
| stalknights_2                | osint     | Sheepiroo   | med    | ✅        | ✅     |
| stalknights_3                | osint     | Sheepiroo   | med    | ✅        | ✅     |
| stalknights_4                | osint     | Sheepiroo   | hard   | ✅        | ✅     |
| stalknights_5                | osint     | Sheepiroo   | med    | ✅        | ✅     |
| super_fan                    | osint     | arepi_nemui | hard   | ✅        | ✅     |
| phase_coffee_1               | pwn       | Sheepiroo   | easy   | ✅        | ❌     |
| phase_coffee_2               | pwn       | Sheepiroo   | med    | ✅        | ❌     |
| phase_coffee_3               | pwn       | Sheepiroo   | med    | ✅        | ❌     |
| awassmbely                   | rev       | lisp_beamer | easy   | ✅        | ❌     |
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

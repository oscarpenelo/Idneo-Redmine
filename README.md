# Idneo Redmine scheduler ![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg)

Idneo Redmine Bot.

## Installation

### Requirements
* Idneo member
* Linux
* Docker or Python 3


## Usage
### Scheduler mode:
Every day at 3:00 pm a day will be tracked (requires docker)

`$ ./start.sh -u [USERNAME] -p [PASSWORD] -i [ISSUEID]`

### Month track mode:

Tracks an entire month:

`$ python redmine.py -u [USERNAME] -p [PASSWORD] -i [ISSUEID] -m [MONTH NUMBER] -y [YEAR] -e [EXCLUDED DAYS]`
`$ python redmine.py --username [USERNAME] --password [PASSWORD] --issueid [ISSUEID] --month [MONTH NUMBER] --year [YEAR] -exclude [EXCLUDED DAYS]`



## License
[GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
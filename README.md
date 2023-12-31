# pycurl [WIP]
curl implemented in python, inspired from the [Coding Challenges](https://codingchallenges.substack.com/p/coding-challenge-41-curl) of [John Cricket](https://twitter.com/johncrickett).

## Usage
- just clone this repo, no need to install any other packages as of now. Requires python3.
- run it from command line, with ```python purl.py [ options ] <url>```
- supported options,
  -  ```-v``` or ```--verbose```  for verbose response
  -   ```-x``` or ```--request_type``` HTTP request type (wip to support all http verbs)
  -   ```-o``` or ```--output_file``` output redirection to any file other than ```STD_OUT```

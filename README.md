# SSof-Project1920

Welcome to the Community Repository for Testing the Projects of the Software Security course 2019/20.

Notice that __these repository is not supervised by the lecturers of the course, hence no guarantees of correctness of the provided examples are provided__. Apply your best judgement when using these tests.

## Submitting a Test

If you want to submit a test, just create folder `TXX-NN` where `XX` is your group number and `NN` is the test sequence number for your group, eg, the 3rd test submitted by group 47 should be `T47-03`.

Add the following files to that folder

- `input.json` with the input slice
- `patterns.json` with the patterns to verify
- `output.json` with the expected output
- `program.py` with the original Python program for convenience of reading

Commit the test to the repository. Add a brief commit message explaining the goal of the test.

## Running a Test

To run a test you should run (eg Python)

`python ./bo-analyser.py <path_to_repo>/program.json <path_to_repo>/patterns.json`

And compare with the result in 

`<path_to_repo>/output.json`

## Spotting incorrect Outputs/Mistakes

In case you find a mistake, please submit an issue detailing the error and assign it to the person that submitted the original test.

If it is clear that it is an error, you can also submit a pull request with the fix and commit message `fixes #Y` where Y is the issue number.

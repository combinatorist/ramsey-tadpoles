# run

```bash
sbt package
```

> If you get errors, try updating to latest 2.13 patch.

Then, when that's packaged successfully,
```
spark-submit --class Main target/scala-2.13/spark-ramsey-numbers_2.13-0.1.jar 4
```
(adjusting the scala patch version and your desired modulo, of course)

# results
Don't be surprised to that it writes to the local [[data]] directory.
That is just a symbolic link. ;) #iJustSavedYouAnHourFool


todo:
- unskew partitions (rotate cycle after setting it)
  - but consider rotating in the input to permutations instead

name := "spark-ramsey-numbers"

version := "0.1"

scalaVersion := "2.13.14"

val sparkVersion = "3.5.0"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-sql" % sparkVersion
)

scalacOptions := Seq("-unchecked", "-deprecation")

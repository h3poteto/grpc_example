import com.trueaccord.scalapb.compiler.Version.{grpcJavaVersion, scalapbVersion, protobufVersion}

name := """grpcScalasample"""

scalaVersion := "2.12.3"

lazy val root = project.in(file("."))

libraryDependencies ++= Seq(
  "io.grpc" % "grpc-netty" % grpcJavaVersion,
  "com.trueaccord.scalapb" %% "scalapb-runtime" % scalapbVersion % "protobuf",
  "com.trueaccord.scalapb" %% "scalapb-runtime-grpc" % scalapbVersion,
  "io.grpc" % "grpc-all" % grpcJavaVersion
)

PB.targets in Compile := Seq(
  scalapb.gen() -> ((sourceManaged in Compile).value / "protobuf-scala")
)



package io.grpc.exmamples.helloworld

import java.util.logging.Logger

import io.grpc.{Server, ServerBuilder}
import helloworld.hello.{GreeterGrpc, HelloRequest, HelloReply}

import scala.concurrent.{ExecutionContext, Future}

object HelloworldServer {
  private val logger = Logger.getLogger(classOf[HelloworldServer].getName)

  def main(args: Array[String]): Unit = {
    val server = new HelloworldServer(ExecutionContext.global)
    server.start()
    server.blockUnitShutdown()
  }

  private val port = 50051
}


class HelloworldServer(executionContext: ExecutionContext) { self =>
  private[this] var server: Server = null

  private def start(): Unit = {
    server = ServerBuilder.forPort(HelloworldServer.port).addService(GreeterGrpc.bindService(new GreeterImpl, executionContext)).build.start
    HelloworldServer.logger.info("Server started, listening on " + HelloworldServer.port)
    sys.addShutdownHook {
      System.err.println("*** shutting down gPRC server since JVM is shutting down")
      self.stop()
      System.err.println("*** server shutdown")
    }
  }

  private def stop(): Unit = {
    if (server != null) {
      server.shutdown()
    }
  }
  private def blockUnitShutdown(): Unit = {
    if (server != null) {
      server.awaitTermination()
    }
  }

  private class GreeterImpl extends GreeterGrpc.Greeter {
    override def sayHello(req: HelloRequest) = {
      val reply = HelloReply(message = "Hello " + req.name)
      Future.successful(reply)
    }
  }
}

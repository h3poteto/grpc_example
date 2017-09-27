package io.grpc.exmamples.server

import java.util.logging.Logger

import io.grpc.{Server, ServerBuilder}
import io.grpc.stub.StreamObserver
import proto.customer_service.{CustomerServiceGrpc, Person, RequestType, ResponseType}

import scala.concurrent.{ExecutionContext, Future}

object CustomerServiceServer {
  private val logger = Logger.getLogger(classOf[CustomerServiceServer].getName)

  def main(args: Array[String]): Unit = {
    val server = new CustomerServiceServer(ExecutionContext.global)
    server.start()
    server.blockUnitShutdown()
  }

  private val port = sys.env.getOrElse("SERVER_PORT", "50051").asInstanceOf[String].toInt
}


class CustomerServiceServer(executionContext: ExecutionContext) { self =>
  private[this] var server: Server = null

  private[this] var personData: Array[Person] = Array.empty

  private def start(): Unit = {
    server = ServerBuilder.forPort(CustomerServiceServer.port).addService(CustomerServiceGrpc.bindService(new CustomerServiceImpl, executionContext)).build.start
    CustomerServiceServer.logger.info("Server started, listening on " + CustomerServiceServer.port)
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

  private class CustomerServiceImpl extends CustomerServiceGrpc.CustomerService {
    override def addPerson(person: Person) = {
      personData = personData :+ person
      val reply = ResponseType()
      Future.successful(reply)
    }

    override def listPerson(req: RequestType, stream: StreamObserver[Person]) = {
      for (p <- personData) {
        stream.onNext(p)
      }
      stream.onCompleted()
    }
  }
}

package cmd

import (
	"fmt"
	"log"
	"os"

	pb "github.com/h3poteto/grpc_example/server/go/proto"
	"github.com/spf13/cobra"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"io"
)

func listCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "list",
		Short: "list persons",
		Run:   list,
	}
	return cmd
}

func list(cmd *cobra.Command, args []string) {
	addr := os.Getenv("SERVER_IP")
	port := os.Getenv("SERVER_PORT")
	conn, err := grpc.Dial(addr+":"+port, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()
	client := pb.NewCustomerServiceClient(conn)

	stream, err := client.ListPerson(context.Background(), new(pb.RequestType))
	if err != nil {
		log.Fatal(err)
	}
	for {
		person, err := stream.Recv()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}
		fmt.Println(person)
	}
	return
}

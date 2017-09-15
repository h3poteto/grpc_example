package cmd

import (
	"log"
	"os"
	"strconv"

	pb "github.com/h3poteto/grpc_example/proto"
	"github.com/spf13/cobra"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

func addCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "add",
		Short: "add a person",
		Run:   add,
	}
	return cmd
}

func add(cmd *cobra.Command, args []string) {
	if len(args) != 2 {
		log.Fatal("invalid arguments")
	}
	name := args[0]
	age, err := strconv.Atoi(args[1])
	if err != nil {
		log.Fatal(err)
	}
	addr := os.Getenv("SERVER_IP")
	port := os.Getenv("SERVER_PORT")
	conn, err := grpc.Dial(addr+":"+port, grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	defer conn.Close()
	client := pb.NewCustomerServiceClient(conn)

	person := &pb.Person{
		Name: name,
		Age:  int32(age),
	}

	_, err = client.AddPerson(context.Background(), person)
	if err != nil {
		log.Fatal(err)
	}
}

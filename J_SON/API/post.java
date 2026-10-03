import java.net.URI;
import java.net.http.*;
import java.nio.file.Files;
import java.nio.file.Path;
public class post {

    public static void main(String[] args) throws Exception {
        HttpClient client =HttpClient.newHttpClient();
        String json = Files.readString(Path.of("J_SON", "API", "first.JSON"));
        HttpRequest request=HttpRequest.newBuilder()
            .uri(URI.create("https://jsonplaceholder.typicode.com/posts"))
            .header("Content-Type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(json))
            .build();
        HttpResponse<String> response=
            client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.statusCode());
        System.out.println(response.body());

    }
}
import 'package:dio/dio.dart';
import 'package:json_annotation/json_annotation.dart';
import 'package:retrofit/retrofit.dart';

part 'app.dart';
part 'order.dart';
part 'client.g.dart';

@RestApi(baseUrl: "http://127.0.0.1:8000/api/")
abstract class RestClient {
  factory RestClient(Dio dio, {String baseUrl}) = _RestClient;

  @GET("/apps")
  Future<List<App>> getApps();

  @GET("/orders")
  Future<List<Order>> getOrders();

  @GET("/orders/{id}")
  Future<Order> getTask(@Path("id") String id);
}

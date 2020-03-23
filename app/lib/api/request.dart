import 'package:dio/dio.dart';
import 'package:eletec/cache/token.dart';

class ApiRequest {

  Dio dio;

  BaseOptions options = new BaseOptions(
    // baseUrl: 'http://eletecapp.com/api/',
    baseUrl: 'http://127.0.0.1:8000/',
    connectTimeout: 5000,
    receiveTimeout: 3000,
  );

  ApiRequest._() {
    dio = new Dio(options)..interceptors.add(new InterceptorsWrapper(
      onRequest: (Options options) async {
        var token = await Token.instance.getToken();
        options.headers['Authorization'] = 'token ' + token;
        return options;
      }
    ));
  }

  static ApiRequest instance = new ApiRequest._();
}
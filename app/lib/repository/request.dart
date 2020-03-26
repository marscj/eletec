import 'package:dio/dio.dart';
import 'package:eletec/repository/token.dart';

class ApiRequest {
  Dio dio;

  ApiRequest._() {
    BaseOptions options = new BaseOptions(
      // baseUrl: 'http://eletecapp.com/api/',
      baseUrl: 'http://127.0.0.1:8000/api/',
      connectTimeout: 5000,
      receiveTimeout: 3000,
    );

    dio = new Dio(options)
      ..interceptors
          .add(new InterceptorsWrapper(onRequest: (Options options) async {
        var token = await TokenRepository().get();
        options.headers['Authorization'] = token;
        return options;
      }, onError: (DioError e) async {
        if (e?.response?.statusCode == 401) {
          TokenRepository().clear();
        }
        return e;
      }));
  }

  static ApiRequest instance = new ApiRequest._();
}

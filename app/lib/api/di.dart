import 'package:dio/dio.dart';
import 'package:eletec/cache/token.dart';

class AuthInterceptor extends Interceptor {
  
  @override
  onRequest(RequestOptions options) async {
    final token = await Token.instance.getToken();
    options.headers.update("Authorization", (_) => token, ifAbsent: () => token);
    return super.onRequest(options);
  }
}

class Api {

  final Dio dio = Dio()
  ..options = BaseOptions(baseUrl: 'http://eletecapp.com/', connectTimeout: 30, receiveTimeout: 30)
  ..interceptors.add(AuthInterceptor())
  ..interceptors.add(LogInterceptor(responseBody: true, requestBody: true));

  Api._();

  static Api instance = new Api._();
}
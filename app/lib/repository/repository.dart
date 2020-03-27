import 'package:dio/dio.dart';

import 'request.dart';
import 'reponse.dart';

abstract class Repository {
  final String path;

  Repository(this.path);

  Future<Response> list({Map<String, dynamic> params}) {
    return ApiRequest.instance.dio
        .get(path, queryParameters: params)
        .then((res) {
      return Response();
    });
  }

  Future<Response> get(int pk) {
    return ApiRequest.instance.dio.get(path + '/$pk/');
  }

  Future<Response> post(Map<String, dynamic> playload) {
    return ApiRequest.instance.dio.post(path, data: playload);
  }

  Future<Response> put(int pk, Map<String, dynamic> playload) {
    return ApiRequest.instance.dio.put(path + '/$pk/', data: playload);
  }

  Future<Response> del(int pk) {
    return ApiRequest.instance.dio.delete(path + '/$pk/');
  }
}

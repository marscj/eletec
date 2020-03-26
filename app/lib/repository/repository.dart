import 'package:dio/dio.dart';

import 'request.dart';

abstract class Repository {
  final String path;

  Repository(this.path);

  Future<Response> list() {
    return ApiRequest.instance.dio.get(path);
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

import 'package:dio/dio.dart';
import 'package:eletec/repository/reponse.dart';
import 'package:eletec/repository/repository.dart';
import 'package:eletec/repository/request.dart';

class AppRepository<Result> implements Repository {
  @override
  Future<Response> del(int pk) {
    // TODO: implement del
    return null;
  }

  @override
  Future<Response> get(int pk) {
    // TODO: implement get
    return null;
  }

  @override
  Future<Response> list({Map<String, dynamic> params}) {
    // TODO: implement list
    return null;
  }

  @override
  // TODO: implement path
  String get path => null;

  @override
  Future<Response> post(Map<String, dynamic> playload) {
    // TODO: implement post
    return null;
  }

  @override
  Future<Response> put(int pk, Map<String, dynamic> playload) {
    // TODO: implement put
    return null;
  }
}

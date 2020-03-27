import 'package:eletec/repository/reponse.dart';
import 'package:eletec/repository/repository.dart';
import 'package:eletec/repository/request.dart';

class AppRepository extends Repository {
  AppRepository() : super('apps/');

  Future<Response> lists({Map<String, dynamic> params}) {
    return ApiRequest.instance.dio.get('path', queryParameters: params);
  }
}

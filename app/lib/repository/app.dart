import 'package:dio/dio.dart';
import 'package:eletec/repository/reponse.dart';
import 'package:eletec/repository/repository.dart';
import 'package:eletec/repository/request.dart';

class AppRepository<Result> implements Repository {
  final path = 'apps/';

  @override
  Future<Result> list({Map<String, dynamic> params}) {
    return ApiRequest.instance.dio
        .get(path, queryParameters: params)
        .then((res) {
      print(res);
      return null;
    });
  }

  noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);
}

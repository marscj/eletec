import 'package:eletec/repository/repository.dart';
import 'package:eletec/repository/request.dart';
import 'package:eletec/model/model.dart';

class AppRepository implements Repository<List<App>> {
  final path = 'apps/';

  @override
  Future<List<App>> list({Map<String, dynamic> params}) {
    return ApiRequest.instance.dio
        .get(path, queryParameters: params)
        .then((res) {
      return null;
    });
  }

  noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);
}

import 'dart:async';

import 'package:rxdart/rxdart.dart';
import 'package:eletec/repository/request.dart';
import 'package:eletec/model/model.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:retrofit/retrofit.dart';

class AppRepository {
  final path = 'apps/';

  Future<List<App>> list(Map<String, dynamic> params) {
    return ApiRequest.instance.dio
        .get(path, queryParameters: params)
        .then((res) {
      return (res.data['result'] as List).map((f) => App.fromJson(f)).toList();
    });
  }

  Stream<String> getAdvertising() {
    return Stream<String>.empty().concatWith([
      SharedPreferences.getInstance().then((sp) {
        return sp.getString('ad');
      }).asStream()
    ]).concatWith([_getAd().asStream()]).distinct();
  }

  Future<String> _getAd() {
    return list({'tag': 0}).then((data) {
      var _data = data.isNotEmpty ? data?.last?.image?.advertising : null;
      _setAd(_data);
      return _data;
    });
  }

  Future<bool> _setAd(String ad) async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.setString('ad', ad);
    });
  }

  noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);
}

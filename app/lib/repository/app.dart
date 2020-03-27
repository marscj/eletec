import 'dart:async';

import 'package:rxdart/rxdart.dart';
import 'package:eletec/repository/repository.dart';
import 'package:eletec/repository/request.dart';
import 'package:eletec/model/model.dart';
import 'package:shared_preferences/shared_preferences.dart';

class AppRepository implements Repository {
  final path = 'apps/';

  @override
  Future<List<App>> list(Map<String, dynamic> params) {
    return ApiRequest.instance.dio
        .get(path, queryParameters: params)
        .then((res) {
      return (res.data['result'] as List).map((f) => App.fromJson(f)).toList();
    });
  }

  Future<String> _ad(Map<String, dynamic> params) {
    return ApiRequest.instance.dio
        .get(path, queryParameters: params)
        .then((res) {
      var data =
          (res.data['result'] as List).map((f) => App.fromJson(f)).toList();
      var item = data.length > 0 ? data?.last?.image?.advertising : null;
      _setAd(item);
      return item;
    });
  }

  Stream<String> getAdvertising() {
    return Stream.fromFuture(SharedPreferences.getInstance().then((sp) {
      return sp.getString('ad');
    })).concatWith([
      _ad({'tag': 0}).asStream().delay(Duration(seconds: 2))
    ]).distinct()
      ..listen((onData) {
        print(onData);
      });
  }

  Future<bool> _setAd(String ad) async {
    return SharedPreferences.getInstance().then((sp) {
      return sp.setString('ad', ad);
    });
  }

  noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);
}

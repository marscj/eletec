

import 'dart:async';
import 'package:eletec/api/api.dart';
import 'package:eletec/view/common/state.dart';
import 'package:rxdart/rxdart.dart';

import 'package:eletec/api/reponse.dart';
import 'package:eletec/view/auth/model.dart';

class Bloc {
  final Stream<BaseState> state;
  final Sink<Model> reqCtl;

  factory Bloc() {
    final reqCtl = BehaviorSubject<Model>();

    final state = reqCtl
        .debounceTime(const Duration(milliseconds: 100))
        .switchMap<BaseState>((Model model) => _call(model))
        .startWith(LoadingState());

    return Bloc._(reqCtl, state);
  }

  Bloc._(this.reqCtl, this.state);

  static Stream<BaseState> _call(Model model) async * {
    yield LoadingState();

    try {
      final result = await new ApiService().phoneValidate(model);
      yield SuccessState(result);
    } catch (e) {
      yield ErrorState();
    }
  }

  void resendOtp(bool flag) {

  }

  void dispose() {
    reqCtl.close();
  }
}


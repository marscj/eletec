

import 'dart:async';
import 'package:rxdart/subjects.dart';

import 'package:eletec/api/reponse.dart';
import 'package:eletec/view/auth/model.dart';

class Bloc {
  final otpController = StreamController<Model>();
  final loginController = StreamController<Model>();
  final apiController = BehaviorSubject<Response>();
  final otpResendController = StreamController<bool>();
  final otpResultController = BehaviorSubject<bool>();

  Sink<Model> get otpSink => otpController.sink;
  Sink<Model> get loginSink => otpController.sink;
  Sink<bool> get resendOtpSink => otpResendController.sink;
  Stream<bool> get otpResult => otpResultController.stream;
  Stream<Response> get apiResult => apiController.stream;

  Bloc () {
    otpController.stream.listen(call);
    otpResendController.stream.listen(resendOtp);
    loginController.stream.listen(call);
  }

  void call(Model payload) async {

  }

  void resendOtp(bool flag) {
    otpResultController.add(false);
  }

  void dispose() {
    otpController.close();
    otpResendController.close();
    apiController.close();
    otpResultController.close();
    loginController.close();
  }
}


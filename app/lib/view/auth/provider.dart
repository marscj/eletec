
import 'package:flutter/material.dart';

class Provider with ChangeNotifier {
  
  String _phone;

  String _otp;

  String get phone => _phone;

  String get otp => _otp;

  Provider(this._phone, this._otp);
}


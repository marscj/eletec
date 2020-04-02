part of 'client.dart';

// ignore_for_file: non_constant_identifier_names

@JsonSerializable()
class Otp extends Equatable {
  final String phone_number;

  Otp(this.phone_number);

  @override
  List<Object> get props => [phone_number];

  static Otp fromJson(Map<String, dynamic> json) =>
      _$OtpFromJson(json);
  Map<String, dynamic> toJson() => _$OtpToJson(this);
}

@JsonSerializable()
class Token extends Equatable {
  final int id;
  final String last_login;
  final String token;

  Token(this.id, this.last_login, this.token);

  @override
  List<Object> get props => [id, last_login, token];

  static Token fromJson(Map<String, dynamic> json) =>
      _$TokenFromJson(json);
  Map<String, dynamic> toJson() => _$TokenToJson(this);
}
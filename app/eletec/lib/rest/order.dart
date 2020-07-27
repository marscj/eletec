part of 'client.dart';

@JsonSerializable()
class Order {
  int id;

  Order({this.id});

  static Order fromJson(Map<String, dynamic> json) => _$OrderFromJson(json);
  Map<String, dynamic> toJson() => _$OrderToJson(this);
}

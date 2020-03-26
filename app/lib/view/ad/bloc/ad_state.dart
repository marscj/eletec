part of 'ad_bloc.dart';

class AdState extends Equatable {
  final int timer;

  const AdState(this.timer);

  @override
  List<Object> get props => [timer];
}

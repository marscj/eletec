part of 'ad_bloc.dart';

abstract class AdState extends Equatable {
  final int timer;

  const AdState(this.timer);

  @override
  List<Object> get props => [timer];
}

class AdInitial extends AdState {
  AdInitial(int timer) : super(timer);
}

class AdRunning extends AdState {
  AdRunning(int timer) : super(timer);
}

import 'package:eletec/view/login_new/main.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import 'view/app/app.dart';
import 'view/loading/loading.dart';

void main() {
  lgoin_main();
  // runApp(
  //   LoadingWidget(
  //     child: BlocProvider<AppBloc>(
  //       create: (context) => AppBloc(context)..add(AppInitial()),
  //       child: BlocBuilder<AppBloc, AppState>(
  //         builder: (context, state) => EletecApp(state)
  //       )
  //     )
  //   )
  // );
}
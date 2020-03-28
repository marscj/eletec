import 'package:eletec/view/login/bloc/login_bloc.dart';
import 'package:eletec/view/widgets/gradient_button.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:intl_phone_number_input/intl_phone_number_input.dart';

class LoginPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Theme(
        data: ThemeData(
            brightness: Brightness.light,
            backgroundColor: Colors.white,
            scaffoldBackgroundColor: Colors.white),
        child: Scaffold(
          body: Stack(
            fit: StackFit.expand,
            children: <Widget>[LoginBackground(), LoginWidgets()],
          ),
        ));
  }
}

class LoginWidgets extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.center,
      child: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            SizedBox.fromSize(size: Size.fromHeight(100)),
            LoginCard()
          ],
        ),
      ),
    );
  }
}

class LoginCard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final deviceSize = MediaQuery.of(context).size;
    return SizedBox(
        height: deviceSize.height / 2 - 10,
        width: deviceSize.width * 0.85,
        child:
            new Card(color: Colors.white, elevation: 2.0, child: LoginForm()));
  }
}

class LoginForm extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocProvider<LoginBloc>(
        create: (_) => LoginBloc(),
        child: BlocListener<LoginBloc, LoginState>(
          listener: (context, state) {},
          child: BlocBuilder<LoginBloc, LoginState>(
            builder: (context, state) {
              return Container(
                padding: EdgeInsets.all(15),
                child: Form(
                    child: Column(
                  children: <Widget>[
                    TextFormField(
                      keyboardType: TextInputType.phone,
                      maxLength: 10,
                      decoration: InputDecoration(
                          labelText: 'Phone Number', prefixText: '+971  '),
                    ),
                    state is LoginOtpState
                        ? TextFormField(
                            keyboardType: TextInputType.number,
                            maxLength: 4,
                            decoration: InputDecoration(
                                labelText: 'OTP', helperText: '4 digits'),
                          )
                        : Container(),
                    SizedBox(height: 40),
                    state is LoginInitState
                        ? Container(
                            child: GradientButton(
                            onPressed: () {
                              BlocProvider.of<LoginBloc>(context)
                                  .add(LoginGetOTP('abc'));
                            },
                            text: 'Get OTP',
                          ))
                        : Container(
                            child: GradientButton(
                            onPressed: () {
                              BlocProvider.of<LoginBloc>(context)
                                  .add(LoginValidate('abc', 'abc'));
                            },
                            text: 'Login',
                          )),
                    state is LoginOtpState
                        ? new FlatButton(
                            child: Text('Resend OTP'),
                            onPressed: () => BlocProvider.of<LoginBloc>(context)
                                .add(LoginResendOTP()))
                        : new Container()
                  ],
                )),
              );
            },
          ),
        ));
  }
}

class LoginBackground extends StatelessWidget {
  LoginBackground();

  Widget topHalf(BuildContext context) {
    return new Flexible(
      flex: 5,
      child: ClipPath(
        clipper: new ArcClipper(),
        child: Stack(
          children: <Widget>[
            new Container(
              width: double.infinity,
              height: double.infinity,
              decoration: new BoxDecoration(
                  gradient: new LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [Colors.black87, Theme.of(context).accentColor],
              )),
            ),
            new Center(
                child: Image.asset(
              'assets/logo.png',
              fit: BoxFit.none,
              color: Colors.blue,
            ))
          ],
        ),
      ),
    );
  }

  final bottomHalf = new Flexible(
    flex: 9,
    child: new Container(),
  );

  @override
  Widget build(BuildContext context) {
    return new Flex(
      direction: Axis.vertical,
      children: <Widget>[topHalf(context), bottomHalf],
    );
  }
}

class ArcClipper extends CustomClipper<Path> {
  @override
  Path getClip(Size size) {
    var path = new Path();
    path.lineTo(0.0, size.height - 30);

    var firstControlPoint = new Offset(size.width / 4, size.height);
    var firstPoint = new Offset(size.width / 2, size.height);
    path.quadraticBezierTo(firstControlPoint.dx, firstControlPoint.dy,
        firstPoint.dx, firstPoint.dy);

    var secondControlPoint =
        new Offset(size.width - (size.width / 4), size.height);
    var secondPoint = new Offset(size.width, size.height - 30);
    path.quadraticBezierTo(secondControlPoint.dx, secondControlPoint.dy,
        secondPoint.dx, secondPoint.dy);

    path.lineTo(size.width, 0.0);
    path.close();

    return path;
  }

  @override
  bool shouldReclip(CustomClipper<Path> oldClipper) => false;
}

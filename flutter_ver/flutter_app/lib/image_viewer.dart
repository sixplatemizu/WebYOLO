import 'dart:io';
import 'package:flutter/material.dart';

class ImageViewerScreen extends StatelessWidget {
  final File originalImage;
  final File processedImage;

  const ImageViewerScreen({Key? key, required this.originalImage, required this.processedImage}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Image Viewer'),
      ),
      body: Column(
        children: [
          Expanded(
            child: Row(
              children: [
          Expanded(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Text(
                        '原始',
                        style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
          ),
                      const SizedBox(height: 10),
                      Container(
                        padding: const EdgeInsets.all(10),
                        child: Image.file(
                          originalImage,
                          fit: BoxFit.contain,
                          height: MediaQuery.of(context).size.height * 0.6,
      ),
                      ),
                    ],
                  ),
                ),
                const VerticalDivider(
                  thickness: 2,
                  color: Colors.grey,
                ),
                Expanded(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      const Text(
                        '处理后',
                        style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                      ),
                      const SizedBox(height: 10),
                      Container(
                        padding: const EdgeInsets.all(10),
                        child: Image.file(
                          processedImage,
                          fit: BoxFit.contain,
                          height: MediaQuery.of(context).size.height * 0.6,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
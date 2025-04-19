import 'dart:io';
import 'package:flutter/material.dart';

class ImageViewerScreen extends StatelessWidget {
  final File originalImage;
  final File processedImage;
  final List<dynamic> keypoints;
  final String mode;

  const ImageViewerScreen({
    Key? key,
    required this.originalImage,
    required this.processedImage,
    this.keypoints = const [],
    required this.mode,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('${mode == 'object' ? 'Object' : 'Pose'} Detection Results'),
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
                        'Original',
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
                const VerticalDivider(thickness: 2, color: Colors.grey),
                Expanded(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        mode == 'object' ? 'Object Detection' : 'Pose Detection',
                        style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
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
          if (mode == 'pose' && keypoints.isNotEmpty)
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: Text(
                'Detected ${keypoints.length} person(s)',
                style: const TextStyle(fontSize: 16),
              ),
      ),
        ],
      ),
    );
  }
}

    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #fafafa; color: #333; }
            h1 { text-align: center; color: #2b5f9e; }
            h2 { color: #444; border-left: 5px solid #2b5f9e; padding-left: 8px; }
            .paper { margin-bottom: 20px; padding: 10px; background-color: #fff; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .title { font-size: 16px; font-weight: bold; }
            .authors { color: #555; font-size: 13px; }
            .abstract { margin-top: 5px; font-size: 14px; color: #444; }
            a { color: #2b5f9e; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>📚 arXiv 语音方向论文日报</h1>
        <p style="text-align:center;">日期：2025-10-13</p>
        <hr>
    <h2>🎵 Text-to-Speech / Speech Synthesis (TTS)</h2>
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11646v1">BridgeCode: A Dual Speech Representation Paradigm for Autoregressive Zero-Shot Text-to-Speech Synthesis</a></div>
                <div class="authors">👥 Jingyuan Xing, Mingru Yang, Zhipeng Li, Xiaofen Xing, Xiangmin Xu</div>
                <div class="abstract">Autoregressive (AR) frameworks have recently achieved remarkable progress in zero-shot text-to-speech (TTS) by leveraging discrete speech tokens and large language model techniques. Despite their success, existing AR-based zero-shot TTS systems face two critical limitations: (i) an inherent speed-quality trade-off, as sequential token generation either reduces frame rates at the cost of expressiveness or enriches tokens at the cost of efficiency, and (ii) a text-oriented supervision mismatch, as...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11124v1">Perturbation Self-Supervised Representations for Cross-Lingual Emotion TTS: Stage-Wise Modeling of Emotion and Speaker</a></div>
                <div class="authors">👥 Cheng Gong, Chunyu Qiang, Tianrui Wang, Yu Jiang, Yuheng Lu, Ruihao Jing, Xiaoxiao Miao, Xiaolei Zhang, Longbiao Wang, Jianwu Dang</div>
                <div class="abstract">Cross-lingual emotional text-to-speech (TTS) aims to produce speech in one language that captures the emotion of a speaker from another language while maintaining the target voice's timbre. This process of cross-lingual emotional speech synthesis presents a complex challenge, necessitating flexible control over emotion, timbre, and language. However, emotion and timbre are highly entangled in speech signals, making fine-grained control challenging. To address this issue, we propose EMM-TTS, a no...</div>
            </div>
            <h2>🌫️ Diffusion / Generative Speech Models</h2>
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11715v1">Point Prompting: Counterfactual Tracking with Video Diffusion Models</a></div>
                <div class="authors">👥 Ayush Shrivastava, Sanyam Mehta, Daniel Geng, Andrew Owens</div>
                <div class="abstract">Trackers and video generators solve closely related problems: the former analyze motion, while the latter synthesize it. We show that this connection enables pretrained video diffusion models to perform zero-shot point tracking by simply prompting them to visually mark points as they move over time. We place a distinctively colored marker at the query point, then regenerate the rest of the video from an intermediate noise level. This propagates the marker across frames, tracing the point's traje...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11690v1">Diffusion Transformers with Representation Autoencoders</a></div>
                <div class="authors">👥 Boyang Zheng, Nanye Ma, Shengbang Tong, Saining Xie</div>
                <div class="abstract">Latent generative modeling, where a pretrained autoencoder maps pixels into a latent space for the diffusion process, has become the standard strategy for Diffusion Transformers (DiT); however, the autoencoder component has barely evolved. Most DiTs continue to rely on the original VAE encoder, which introduces several limitations: outdated backbones that compromise architectural simplicity, low-dimensional latent spaces that restrict information capacity, and weak representations that result fr...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11683v1">Boundary-Guided Policy Optimization for Memory-efficient RL of Diffusion Large Language Models</a></div>
                <div class="authors">👥 Nianyi Lin, Jiajie Zhang, Lei Hou, Juanzi Li</div>
                <div class="abstract">A key challenge in applying reinforcement learning (RL) to diffusion large language models (dLLMs) lies in the intractability of their likelihood functions, which are essential for the RL objective, necessitating corresponding approximation in each training step. While existing methods approximate the log-likelihoods by their evidence lower bounds (ELBOs) via customized Monte Carlo (MC) sampling, the forward computational graphs of all MC samples need to be retained for the gradient computation ...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11650v1">InfiniHuman: Infinite 3D Human Creation with Precise Control</a></div>
                <div class="authors">👥 Yuxuan Xue, Xianghui Xie, Margaret Kostyrko, Gerard Pons-Moll</div>
                <div class="abstract">Generating realistic and controllable 3D human avatars is a long-standing challenge, particularly when covering broad attribute ranges such as ethnicity, age, clothing styles, and detailed body shapes. Capturing and annotating large-scale human datasets for training generative models is prohibitively expensive and limited in scale and diversity. The central question we address in this paper is: Can existing foundation models be distilled to generate theoretically unbounded, richly annotated 3D h...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11590v1">Diffusion-DFL: Decision-focused Diffusion Models for Stochastic Optimization</a></div>
                <div class="authors">👥 Zihao Zhao, Christopher Yeh, Lingkai Kong, Kai Wang</div>
                <div class="abstract">Decision-focused learning (DFL) integrates predictive modeling and optimization by training predictors to optimize the downstream decision target rather than merely minimizing prediction error. To date, existing DFL methods typically rely on deterministic point predictions, which are often insufficient to capture the intrinsic stochasticity of real-world environments. To address this challenge, we propose the first diffusion-based DFL approach, which trains a diffusion model to represent the dis...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11567v1">A Framework for Low-Effort Training Data Generation for Urban Semantic Segmentation</a></div>
                <div class="authors">👥 Denis Zavadski, Damjan Kalšan, Tim Küchler, Haebom Lee, Stefan Roth, Carsten Rother</div>
                <div class="abstract">Synthetic datasets are widely used for training urban scene recognition models, but even highly realistic renderings show a noticeable gap to real imagery. This gap is particularly pronounced when adapting to a specific target domain, such as Cityscapes, where differences in architecture, vegetation, object appearance, and camera characteristics limit downstream performance. Closing this gap with more detailed 3D modelling would require expensive asset and scene design, defeating the purpose of ...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11566v1">SCOOP'D: Learning Mixed-Liquid-Solid Scooping via Sim2Real Generative Policy</a></div>
                <div class="authors">👥 Kuanning Wang, Yongchong Gu, Yuqian Fu, Zeyu Shangguan, Sicheng He, Xiangyang Xue, Yanwei Fu, Daniel Seita</div>
                <div class="abstract">Scooping items with tools such as spoons and ladles is common in daily life, ranging from assistive feeding to retrieving items from environmental disaster sites. However, developing a general and autonomous robotic scooping policy is challenging since it requires reasoning about complex tool-object interactions. Furthermore, scooping often involves manipulating deformable objects, such as granular media or liquids, which is challenging due to their infinite-dimensional configuration spaces and ...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11538v1">Massive Activations are the Key to Local Detail Synthesis in Diffusion Transformers</a></div>
                <div class="authors">👥 Chaofan Gan, Zicheng Zhao, Yuanpeng Tu, Xi Chen, Ziran Qin, Tieyuan Chen, Mehrtash Harandi, Weiyao Lin</div>
                <div class="abstract">Diffusion Transformers (DiTs) have recently emerged as a powerful backbone for visual generation. Recent observations reveal \emph{Massive Activations} (MAs) in their internal feature maps, yet their function remains poorly understood. In this work, we systematically investigate these activations to elucidate their role in visual generation. We found that these massive activations occur across all spatial tokens, and their distribution is modulated by the input timestep embeddings. Importantly, ...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11512v1">LikePhys: Evaluating Intuitive Physics Understanding in Video Diffusion Models via Likelihood Preference</a></div>
                <div class="authors">👥 Jianhao Yuan, Fabio Pizzati, Francesco Pinto, Lars Kunze, Ivan Laptev, Paul Newman, Philip Torr, Daniele De Martini</div>
                <div class="abstract">Intuitive physics understanding in video diffusion models plays an essential role in building general-purpose physically plausible world simulators, yet accurately evaluating such capacity remains a challenging task due to the difficulty in disentangling physics correctness from visual appearance in generation. To the end, we introduce LikePhys, a training-free method that evaluates intuitive physics in video diffusion models by distinguishing physically valid and impossible videos using the den...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11499v1">Offline Reinforcement Learning with Generative Trajectory Policies</a></div>
                <div class="authors">👥 Xinsong Feng, Leshu Tang, Chenan Wang, Haipeng Chen</div>
                <div class="abstract">Generative models have emerged as a powerful class of policies for offline reinforcement learning (RL) due to their ability to capture complex, multi-modal behaviors. However, existing methods face a stark trade-off: slow, iterative models like diffusion policies are computationally expensive, while fast, single-step models like consistency policies often suffer from degraded performance. In this paper, we demonstrate that it is possible to bridge this gap. The key to moving beyond the limitatio...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11481v1">Introduction to quantitative De Giorgi methods</a></div>
                <div class="authors">👥 Giovanni Brigati, Clément Mouhot</div>
                <div class="abstract">The theory of De Giorgi (1958) and Nash (1959) solves Hilbert's 19th problem and constitutes a major advance in the analysis of PDEs in the 20th century. This theory concerns the H\"older regularity of solutions to elliptic and parabolic equations with non-regular coefficients, and it was extended by Moser (1960) to include the Harnack inequality. This course reviews the classical De Giorgi method in the elliptic and parabolic cases and introduces its recent extension to hypoelliptic equations w...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11462v1">Unifying Deductive and Abductive Reasoning in Knowledge Graphs with Masked Diffusion Model</a></div>
                <div class="authors">👥 Yisen Gao, Jiaxin Bai, Yi Huang, Xingcheng Fu, Qingyun Sun, Yangqiu Song</div>
                <div class="abstract">Deductive and abductive reasoning are two critical paradigms for analyzing knowledge graphs, enabling applications from financial query answering to scientific discovery. Deductive reasoning on knowledge graphs usually involves retrieving entities that satisfy a complex logical query, while abductive reasoning generates plausible logical hypotheses from observations. Despite their clear synergistic potential, where deduction can validate hypotheses and abduction can uncover deeper logical patter...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11346v1">Uncertainty-Aware ControlNet: Bridging Domain Gaps with Synthetic Image Generation</a></div>
                <div class="authors">👥 Joshua Niemeijer, Jan Ehrhardt, Heinz Handels, Hristina Uzunova</div>
                <div class="abstract">Generative Models are a valuable tool for the controlled creation of high-quality image data. Controlled diffusion models like the ControlNet have allowed the creation of labeled distributions. Such synthetic datasets can augment the original training distribution when discriminative models, like semantic segmentation, are trained. However, this augmentation effect is limited since ControlNets tend to reproduce the original training distribution.   This work introduces a method to utilize data f...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11335v1">DiffStyleTS: Diffusion Model for Style Transfer in Time Series</a></div>
                <div class="authors">👥 Mayank Nagda, Phil Ostheimer, Justus Arweiler, Indra Jungjohann, Jennifer Werner, Dennis Wagner, Aparna Muraleedharan, Pouya Jafari, Jochen Schmid, Fabian Jirasek, Jakob Burger, Michael Bortz, Hans Hasse, Stephan Mandt, Marius Kloft, Sophie Fellenz</div>
                <div class="abstract">Style transfer combines the content of one signal with the style of another. It supports applications such as data augmentation and scenario simulation, helping machine learning models generalize in data-scarce domains. While well developed in vision and language, style transfer methods for time series data remain limited. We introduce DiffTSST, a diffusion-based framework that disentangles a time series into content and style representations via convolutional encoders and recombines them throug...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11330v1">Diffusion-Link: Diffusion Probabilistic Model for Bridging the Audio-Text Modality Gap</a></div>
                <div class="authors">👥 KiHyun Nam, Jongmin Choi, Hyeongkeun Lee, Jungwoo Heo, Joon Son Chung</div>
                <div class="abstract">Contrastive audio-language pretraining yields powerful joint representations, yet a persistent audio-text modality gap limits the benefits of coupling multimodal encoders with large language models (LLMs). We present Diffusion-Link, a diffusion-based modality-bridging module that generatively maps audio embeddings into the text-embedding distribution. The module is trained at the output embedding from the frozen multimodal encoder and implemented as a lightweight network with three residual MLP ...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11325v1">A model reduction method based on nonlinear optimization for multiscale stochastic optimal control problems</a></div>
                <div class="authors">👥 Jingyi Zhang</div>
                <div class="abstract">This paper presents a nonlinear optimization-based model reduction method for multiscale stochastic optimal control problems governed by stochastic partial differential equations. The proposed approach constructs a non-intrusive, data-driven reduced-order model by employing a parameter-separable structure to handle stochastic dependencies and directly minimizing the L2 norm of the output error via gradient-based optimization. Compared to existing methods, this framework offers three significant ...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11301v1">TDADL-IE: A Deep Learning-Driven Cryptographic Architecture for Medical Image Security</a></div>
                <div class="authors">👥 Junhua Zhou, Quanjun Li, Weixuan Li, Guang Yu, Yihua Shao, Yihang Dong, Mengqian Wang, Zimeng Li, Changwei Gong, Xuhang Chen</div>
                <div class="abstract">The rise of digital medical imaging, like MRI and CT, demands strong encryption to protect patient data in telemedicine and cloud storage. Chaotic systems are popular for image encryption due to their sensitivity and unique characteristics, but existing methods often lack sufficient security. This paper presents the Three-dimensional Diffusion Algorithm and Deep Learning Image Encryption system (TDADL-IE), built on three key elements. First, we propose an enhanced chaotic generator using an LSTM...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11245v1">Learning the Structure of Connection Graphs</a></div>
                <div class="authors">👥 Leonardo Di Nino, Gabriele D'Acunto, Sergio Barbarossa, Paolo Di Lorenzo</div>
                <div class="abstract">Connection graphs (CGs) extend traditional graph models by coupling network topology with orthogonal transformations, enabling the representation of global geometric consistency. They play a key role in applications such as synchronization, Riemannian signal processing, and neural sheaf diffusion. In this work, we address the inverse problem of learning CGs directly from observed signals. We propose a principled framework based on maximum pseudo-likelihood under a consistency assumption, which e...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11214v1">CSI Prediction Using Diffusion Models</a></div>
                <div class="authors">👥 Mehdi Sattari, Javad Aliakbari, Alexandre Graell i Amat, Tommy Svensson</div>
                <div class="abstract">Acquiring accurate channel state information (CSI) is critical for reliable and efficient wireless communication, but challenges such as high pilot overhead and channel aging hinder timely and accurate CSI acquisition. CSI prediction, which forecasts future CSI from historical observations, offers a promising solution. Recent deep learning approaches, including recurrent neural networks and Transformers, have achieved notable success but typically learn deterministic mappings, limiting their abi...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11146v1">The evolution of CH in Planck Galactic Cold Clumps</a></div>
                <div class="authors">👥 Gan Luo, Arshia M. Jacob, Marco Padovani, Daniele Galli, Ana López-Sepulcre, Ningyu Tang, Di Li, Jing Zhou, Pei Zuo</div>
                <div class="abstract">Methylidyne (CH) has long been considered a reliable tracer of molecular gas in the low-to-intermediate extinction range. Although extended CH 3.3 GHz emission is commonly observed in diffuse and translucent clouds, observations in cold, dense clumps are rare. In this work, we conducted high-sensitivity CH observations toward 27 PGCCs with the Arecibo 305m telescope. Toward each source, the CH data were analyzed in conjunction with $^{13}$CO (1--0), HINSA, and H$_2$ column densities. Our results...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11117v1">Demystifying Numerosity in Diffusion Models -- Limitations and Remedies</a></div>
                <div class="authors">👥 Yaqi Zhao, Xiaochen Wang, Li Dong, Wentao Zhang, Yuhui Yuan</div>
                <div class="abstract">Numerosity remains a challenge for state-of-the-art text-to-image generation models like FLUX and GPT-4o, which often fail to accurately follow counting instructions in text prompts. In this paper, we aim to study a fundamental yet often overlooked question: Can diffusion models inherently generate the correct number of objects specified by a textual prompt simply by scaling up the dataset and model size? To enable rigorous and reproducible evaluation, we construct a clean synthetic numerosity b...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11107v1">MoMaps: Semantics-Aware Scene Motion Generation with Motion Maps</a></div>
                <div class="authors">👥 Jiahui Lei, Kyle Genova, George Kopanas, Noah Snavely, Leonidas Guibas</div>
                <div class="abstract">This paper addresses the challenge of learning semantically and functionally meaningful 3D motion priors from real-world videos, in order to enable prediction of future 3D scene motion from a single input image. We propose a novel pixel-aligned Motion Map (MoMap) representation for 3D scene motion, which can be generated from existing generative image models to facilitate efficient and effective motion prediction. To learn meaningful distributions over motion, we create a large-scale database of...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11096v1">CoDefend: Cross-Modal Collaborative Defense via Diffusion Purification and Prompt Optimization</a></div>
                <div class="authors">👥 Fengling Zhu, Boshi Liu, Jingyu Hua, Sheng Zhong</div>
                <div class="abstract">Multimodal Large Language Models (MLLMs) have achieved remarkable success in tasks such as image captioning, visual question answering, and cross-modal reasoning by integrating visual and textual modalities. However, their multimodal nature also exposes them to adversarial threats, where attackers can perturb either modality or both jointly to induce harmful, misleading, or policy violating outputs. Existing defense strategies, such as adversarial training and input purification, face notable li...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11057v1">Temporal Alignment Guidance: On-Manifold Sampling in Diffusion Models</a></div>
                <div class="authors">👥 Youngrok Park, Hojung Jung, Sangmin Bae, Se-Young Yun</div>
                <div class="abstract">Diffusion models have achieved remarkable success as generative models. However, even a well-trained model can accumulate errors throughout the generation process. These errors become particularly problematic when arbitrary guidance is applied to steer samples toward desired properties, which often breaks sample fidelity. In this paper, we propose a general solution to address the off-manifold phenomenon observed in diffusion models. Our approach leverages a time predictor to estimate deviations...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11052v1">Latent Refinement Decoding: Enhancing Diffusion-Based Language Models by Refining Belief States</a></div>
                <div class="authors">👥 Qinglin Zhu, Yizhen Yao, Runcong Zhao, Yanzheng Xiang, Amrutha Saseendran, Chen Jin, Philip Alexander Teare, Bin Liang, Yulan He, Lin Gui</div>
                <div class="abstract">Autoregressive (AR) models remain the standard for natural language generation but still suffer from high latency due to strictly sequential decoding. Recent diffusion-inspired approaches, such as LlaDA and Dream, mitigate this by generating in parallel, yet they suffer from two core limitations: information loss, as predictive distributions for non-finalized tokens are discarded at each step, and premature commitment, where local decisions are made without sufficient global coordination. We int...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11050v1">Zero-shot Face Editing via ID-Attribute Decoupled Inversion</a></div>
                <div class="authors">👥 Yang Hou, Minggu Wang, Jianjun Zhao</div>
                <div class="abstract">Recent advancements in text-guided diffusion models have shown promise for general image editing via inversion techniques, but often struggle to maintain ID and structural consistency in real face editing tasks. To address this limitation, we propose a zero-shot face editing method based on ID-Attribute Decoupled Inversion. Specifically, we decompose the face representation into ID and attribute features, using them as joint conditions to guide both the inversion and the reverse diffusion proces...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11038v1">Microscopic description of the proton halo in $^{12}$N</a></div>
                <div class="authors">👥 K. Y. Zhang, X. X. Lu</div>
                <div class="abstract">The year 2025 marks the 40th anniversary of the discovery of halo nuclei and the 15th anniversary of the development of the deformed relativistic Hartree-Bogoliubov theory in continuum (DRHBc). In this work, we present the first DRHBc description of the proton halo phenomenon. The available experimental proton separation energies and empirical matter root-mean-square (rms) radii are reasonably well reproduced for the $N=5$ isotones, ranging from the stable nucleus $^{9}$Be to the drip-line nucle...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11030v1">Resonant W and Z Boson Production in FSRQ Jets: Implications for Diffuse Neutrino Fluxes</a></div>
                <div class="authors">👥 J. -H. Ha, I. Alikhanov</div>
                <div class="abstract">Blazars, particularly Flat Spectrum Radio Quasars (FSRQs), are well-known for their ability to accelerate a substantial population of electrons and positrons, as inferred from multiwavelength radiation observations. Therefore, these astrophysical objects are promising candidates for studying high-energy electron--positron interactions, such as the production of $W^{\pm}$ and $Z$ bosons. In this work, we explore the implications of electron--positron annihilation processes in the jet environments...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11023v1">Parareal in time and spectral in space fast L1 quasilinear subdiffusion solver</a></div>
                <div class="authors">👥 Josefa Caballero, Łukasz Płociniczak, Kishin Sadarangani</div>
                <div class="abstract">We consider the initial-boundary value problem for a quasilinear time-fractional diffusion equation, and develop a fully discrete solver combining the parareal algorithm in time with a L1 finite-difference approximation of the Caputo derivative and a spectral Galerkin discretization in space. Our main contribution is the first rigorous convergence proof for the parareal-L1 scheme in this nonlinear subdiffusive setting. By constructing suitable energy norms and exploiting the orthogonality of the...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11022v1">Fast radio bursts shed light on direct gravity test on cosmological scales</a></div>
                <div class="authors">👥 Shuren Zhou, Pengjie Zhang</div>
                <div class="abstract">A key measure of gravity is the relation between the Weyl potential $\Psi+\Phi$ and the matter overdensity $\delta_m$, capsulized as an effective gravitational constant $G_{\rm light}$ for light motion. Its value, together with the possible spatial and temporal variation, is essential in probing physics beyond Einstein gravity. However, the lack of an unbiased proxy of $\delta_m$ prohibits direct measurement of $G_{\rm light}$. We point out that the equivalence principle ensures the dispersion m...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11013v1">Spatial and Temporal Boundaries in Difference-in-Differences: A Framework from Navier-Stokes Equation</a></div>
                <div class="authors">👥 Tatsuru Kikuchi</div>
                <div class="abstract">This paper develops a unified framework for identifying spatial and temporal boundaries of treatment effects in difference-in-differences designs. Starting from fundamental fluid dynamics equations (Navier-Stokes), we derive conditions under which treatment effects decay exponentially in space and time, enabling researchers to calculate explicit boundaries beyond which effects become undetectable. The framework encompasses both linear (pure diffusion) and nonlinear (advection-diffusion with chem...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11000v1">ContextGen: Contextual Layout Anchoring for Identity-Consistent Multi-Instance Generation</a></div>
                <div class="authors">👥 Ruihang Xu, Dewei Zhou, Fan Ma, Yi Yang</div>
                <div class="abstract">Multi-instance image generation (MIG) remains a significant challenge for modern diffusion models due to key limitations in achieving precise control over object layout and preserving the identity of multiple distinct subjects. To address these limitations, we introduce ContextGen, a novel Diffusion Transformer framework for multi-instance generation that is guided by both layout and reference images. Our approach integrates two key technical contributions: a Contextual Layout Anchoring (CLA) me...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.10993v1">Perspective-aware 3D Gaussian Inpainting with Multi-view Consistency</a></div>
                <div class="authors">👥 Yuxin Cheng, Binxiao Huang, Taiqiang Wu, Wenyong Zhou, Chenchen Ding, Zhengwu Liu, Graziano Chesi, Ngai Wong</div>
                <div class="abstract">3D Gaussian inpainting, a critical technique for numerous applications in virtual reality and multimedia, has made significant progress with pretrained diffusion models. However, ensuring multi-view consistency, an essential requirement for high-quality inpainting, remains a key challenge. In this work, we present PAInpainter, a novel approach designed to advance 3D Gaussian inpainting by leveraging perspective-aware content propagation and consistency verification across multi-view inpainted im...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.10968v1">Blade: A Derivative-free Bayesian Inversion Method using Diffusion Priors</a></div>
                <div class="authors">👥 Hongkai Zheng, Austin Wang, Zihui Wu, Zhengyu Huang, Ricardo Baptista, Yisong Yue</div>
                <div class="abstract">Derivative-free Bayesian inversion is an important task in many science and engineering applications, particularly when computing the forward model derivative is computationally and practically challenging. In this paper, we introduce Blade, which can produce accurate and well-calibrated posteriors for Bayesian inversion using an ensemble of interacting particles. Blade leverages powerful data-driven priors based on diffusion models, and can handle nonlinear forward models that permit only black...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.10918v1">DreamMakeup: Face Makeup Customization using Latent Diffusion Models</a></div>
                <div class="authors">👥 Geon Yeong Park, Inhwa Han, Serin Yang, Yeobin Hong, Seongmin Jeong, Heechan Jeon, Myeongjin Goh, Sung Won Yi, Jin Nam, Jong Chul Ye</div>
                <div class="abstract">The exponential growth of the global makeup market has paralleled advancements in virtual makeup simulation technology. Despite the progress led by GANs, their application still encounters significant challenges, including training instability and limited customization capabilities. Addressing these challenges, we introduce DreamMakup - a novel training-free Diffusion model based Makeup Customization method, leveraging the inherent advantages of diffusion models for superior controllability and ...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.10910v1">SceneTextStylizer: A Training-Free Scene Text Style Transfer Framework with Diffusion Model</a></div>
                <div class="authors">👥 Honghui Yuan, Keiji Yanai</div>
                <div class="abstract">With the rapid development of diffusion models, style transfer has made remarkable progress. However, flexible and localized style editing for scene text remains an unsolved challenge. Although existing scene text editing methods have achieved text region editing, they are typically limited to content replacement and simple styles, which lack the ability of free-style transfer. In this paper, we introduce SceneTextStylizer, a novel training-free diffusion-based framework for flexible and high-fi...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.10894v1">Multiscale Graph Reduction for Heterogeneous and Anisotropic Discrete Diffusion Processes</a></div>
                <div class="authors">👥 Maria Vasilyeva, James Brannick, Ben S. Southworth</div>
                <div class="abstract">We present multiscale graph-based reduction algorithms for upscaling heterogeneous and anisotropic diffusion problems. The proposed coarsening approaches begin by constructing a partitioning of the computational domain into a set of balanced local subdomains, resulting in a standard type of domain decomposition. Given this initial decomposition, general coarsening techniques based on spectral clustering are applied within each subgraph in order to accurately identify the key microscopic features...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.10888v1">Structural encoding with classical codes for computational-basis bit-flip correction in the early fault-tolerant regime</a></div>
                <div class="authors">👥 IlKwon Sohn, Changyeol Lee, Wooyeong Song, Kwangil Bae, Wonhyuk Lee</div>
                <div class="abstract">Achieving reliable performance on early fault-tolerant quantum hardware will depend on protocols that manage noise without incurring prohibitive overhead. We propose a novel framework that integrates quantum computation with the functionality of classical error correction. In this approach, quantum computation is performed within the codeword subspace defined by a classical error correction code. The correction of various types of errors that manifest as bit flips is carried out based on the fin...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.10868v1">FastHMR: Accelerating Human Mesh Recovery via Token and Layer Merging with Diffusion Decoding</a></div>
                <div class="authors">👥 Soroush Mehraban, Andrea Iaboni, Babak Taati</div>
                <div class="abstract">Recent transformer-based models for 3D Human Mesh Recovery (HMR) have achieved strong performance but often suffer from high computational cost and complexity due to deep transformer architectures and redundant tokens. In this paper, we introduce two HMR-specific merging strategies: Error-Constrained Layer Merging (ECLM) and Mask-guided Token Merging (Mask-ToMe). ECLM selectively merges transformer layers that have minimal impact on the Mean Per Joint Position Error (MPJPE), while Mask-ToMe focu...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.10978v1">Does LLM Focus on the Right Words? Diagnosing Language Bias in LLM-based Recommenders</a></div>
                <div class="authors">👥 Bohao Wang, Jiawei Chen, Feng Liu, Changwang Zhang, Jun Wang, Canghong Jin, Chun Chen, Can Wang</div>
                <div class="abstract">Large language models (LLMs), owing to their extensive open-domain knowledge and semantic reasoning capabilities, have been increasingly integrated into recommender systems (RS). However, a substantial gap remains between the pre-training objectives of LLMs and the specific requirements of recommendation tasks. To address this gap, supervised fine-tuning (SFT) is commonly performed on specially curated recommendation datasets to further enhance their predictive ability. Despite its success, SFT ...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11083v1">Flow Matching-Based Autonomous Driving Planning with Advanced Interactive Behavior Modeling</a></div>
                <div class="authors">👥 Tianyi Tan, Yinan Zheng, Ruiming Liang, Zexu Wang, Kexin Zheng, Jinliang Zheng, Jianxiong Li, Xianyuan Zhan, Jingjing Liu</div>
                <div class="abstract">Modeling interactive driving behaviors in complex scenarios remains a fundamental challenge for autonomous driving planning. Learning-based approaches attempt to address this challenge with advanced generative models, removing the dependency on over-engineered architectures for representation fusion. However, brute-force implementation by simply stacking transformer blocks lacks a dedicated mechanism for modeling interactive behaviors that are common in real driving scenarios. The scarcity of in...</div>
            </div>
            <h2>🧠 Speech Foundation / Pretrained Models</h2>
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11576v1">Benchmarking foundation models for hyperspectral image classification: Application to cereal crop type mapping</a></div>
                <div class="authors">👥 Walid Elbarz, Mohamed Bourriz, Hicham Hajji, Hamd Ait Abdelali, François Bourzeix</div>
                <div class="abstract">Foundation models are transforming Earth observation, but their potential for hyperspectral crop mapping remains underexplored. This study benchmarks three foundation models for cereal crop mapping using hyperspectral imagery: HyperSigma, DOFA, and Vision Transformers pre-trained on the SpectralEarth dataset (a large multitemporal hyperspectral archive). Models were fine-tuned on manually labeled data from a training region and evaluated on an independent test region. Performance was measured wi...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.10939v1">Packaging of Low-Environmental-Sensitivity WGM Resonators for Practical Applications</a></div>
                <div class="authors">👥 Jiajun Wu, Xuanqi Wang, Chengyu Zhang, Chenghong Li, Shan Zhong, Songbai Kang</div>
                <div class="abstract">We present a prism-coupled packaging strategy for whispering-gallery mode resonators (WGMRs). Utilizing an all-solid-state optical adhesive process with active temperature control and hermetic sealing, the package exhibits exceptional long-term stability and environmental robustness. A standalone WGMR module was characterized, demonstrating a temperature sensitivity below 10^-7 /{\deg}C and a low-frequency Z-axis acceleration sensitivity below 10^-10 /g. The module was applied as a stable optica...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11562v1">Optimal parallelisation strategies for flat histogram Monte Carlo sampling</a></div>
                <div class="authors">👥 Hubert J. Naguszewski, Christopher D. Woodgate, David Quigley</div>
                <div class="abstract">Flat histogram methods, such as Wang-Landau sampling, provide a means for high throughput calculation of phase diagrams of atomistic/lattice model systems. Many parallelisation schemes with varying degrees of complexity have been proposed to accelerate such sampling simulations. In this study, several widely used schemes are benchmarked - both in isolation and in combination - to establish best practice. The schemes studied include energy domain decomposition with both static sizing of energy su...</div>
            </div>
            <h2>🧩 Multimodal / Audio-Language Models</h2>
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11454v1">Audio-Maestro: Enhancing Large Audio-Language Models with Tool-Augmented Reasoning</a></div>
                <div class="authors">👥 Kuan-Yi Lee, Tsung-En Lin, Hung-Yi Lee</div>
                <div class="abstract">Recent advancements in large multimodal models (LMMs) have shown strong capabilities in audio understanding. However, most systems rely solely on end-to-end reasoning, limiting interpretability and accuracy for tasks that require structured knowledge or specialized signal analysis. In this work, we present Audio-Maestro -- a tool-augmented audio reasoning framework that enables audio-language models to autonomously call external tools and integrate their timestamped outputs into the reasoning pr...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11098v1">VCB Bench: An Evaluation Benchmark for Audio-Grounded Large Language Model Conversational Agents</a></div>
                <div class="authors">👥 Jiliang Hu, Wenfu Wang, Zuchao Li, Chenxing Li, Yiyang Zhao, Hanzhao Li, Liqiang Zhang, Meng Yu, Dong Yu</div>
                <div class="abstract">Recent advances in large audio language models (LALMs) have greatly enhanced multimodal conversational systems. However, existing benchmarks remain limited -- they are mainly English-centric, rely on synthetic speech, and lack comprehensive, discriminative evaluation across multiple dimensions. To address these gaps, we present Voice Chat Bot Bench (VCB Bench) -- a high-quality Chinese benchmark built entirely on real human speech. VCB Bench evaluates LALMs from three complementary perspectives:...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11330v1">Diffusion-Link: Diffusion Probabilistic Model for Bridging the Audio-Text Modality Gap</a></div>
                <div class="authors">👥 KiHyun Nam, Jongmin Choi, Hyeongkeun Lee, Jungwoo Heo, Joon Son Chung</div>
                <div class="abstract">Contrastive audio-language pretraining yields powerful joint representations, yet a persistent audio-text modality gap limits the benefits of coupling multimodal encoders with large language models (LLMs). We present Diffusion-Link, a diffusion-based modality-bridging module that generatively maps audio embeddings into the text-embedding distribution. The module is trained at the output embedding from the frozen multimodal encoder and implemented as a lightweight network with three residual MLP ...</div>
            </div>
            <h2>🎭 Speaker, Emotion & Style Modeling</h2>
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11346v1">Uncertainty-Aware ControlNet: Bridging Domain Gaps with Synthetic Image Generation</a></div>
                <div class="authors">👥 Joshua Niemeijer, Jan Ehrhardt, Heinz Handels, Hristina Uzunova</div>
                <div class="abstract">Generative Models are a valuable tool for the controlled creation of high-quality image data. Controlled diffusion models like the ControlNet have allowed the creation of labeled distributions. Such synthetic datasets can augment the original training distribution when discriminative models, like semantic segmentation, are trained. However, this augmentation effect is limited since ControlNets tend to reproduce the original training distribution.   This work introduces a method to utilize data f...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11335v1">DiffStyleTS: Diffusion Model for Style Transfer in Time Series</a></div>
                <div class="authors">👥 Mayank Nagda, Phil Ostheimer, Justus Arweiler, Indra Jungjohann, Jennifer Werner, Dennis Wagner, Aparna Muraleedharan, Pouya Jafari, Jochen Schmid, Fabian Jirasek, Jakob Burger, Michael Bortz, Hans Hasse, Stephan Mandt, Marius Kloft, Sophie Fellenz</div>
                <div class="abstract">Style transfer combines the content of one signal with the style of another. It supports applications such as data augmentation and scenario simulation, helping machine learning models generalize in data-scarce domains. While well developed in vision and language, style transfer methods for time series data remain limited. We introduce DiffTSST, a diffusion-based framework that disentangles a time series into content and style representations via convolutional encoders and recombines them throug...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.10910v1">SceneTextStylizer: A Training-Free Scene Text Style Transfer Framework with Diffusion Model</a></div>
                <div class="authors">👥 Honghui Yuan, Keiji Yanai</div>
                <div class="abstract">With the rapid development of diffusion models, style transfer has made remarkable progress. However, flexible and localized style editing for scene text remains an unsolved challenge. Although existing scene text editing methods have achieved text region editing, they are typically limited to content replacement and simple styles, which lack the ability of free-style transfer. In this paper, we introduce SceneTextStylizer, a novel training-free diffusion-based framework for flexible and high-fi...</div>
            </div>
            
            <div class="paper">
                <div class="title"><a href="http://arxiv.org/abs/2510.11098v1">VCB Bench: An Evaluation Benchmark for Audio-Grounded Large Language Model Conversational Agents</a></div>
                <div class="authors">👥 Jiliang Hu, Wenfu Wang, Zuchao Li, Chenxing Li, Yiyang Zhao, Hanzhao Li, Liqiang Zhang, Meng Yu, Dong Yu</div>
                <div class="abstract">Recent advances in large audio language models (LALMs) have greatly enhanced multimodal conversational systems. However, existing benchmarks remain limited -- they are mainly English-centric, rely on synthetic speech, and lack comprehensive, discriminative evaluation across multiple dimensions. To address these gaps, we present Voice Chat Bot Bench (VCB Bench) -- a high-quality Chinese benchmark built entirely on real human speech. VCB Bench evaluates LALMs from three complementary perspectives:...</div>
            </div>
            <hr><p style='text-align:center;'>✅ 数据来源：<a href='https://arxiv.org'>arXiv.org</a></p></body></html>
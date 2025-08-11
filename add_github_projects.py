import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from projects.models import Project

def add_github_projects():
    Project.objects.all().delete()
    
    projects_data = [
        {
            'title': 'Federated Learning for Cyber-Physical Systems Security',
            'description': 'Research on federated learning models for securing cyber-physical systems',
            'content': '''This project explores the application of federated learning techniques to enhance the security of cyber-physical systems. The research focuses on developing distributed machine learning approaches that can protect critical infrastructure without compromising data privacy.

## Key Features:
- **Distributed Security Models**: Implementation of federated learning algorithms for cybersecurity
- **Privacy-Preserving**: Maintains data privacy while enabling collaborative security learning
- **Cyber-Physical Systems Focus**: Specifically designed for industrial and critical infrastructure applications
- **Real-time Threat Detection**: Enables real-time security monitoring and threat response

## Technical Approach:
The project utilizes advanced federated learning frameworks to create robust security models that can operate across distributed cyber-physical systems while maintaining data locality and privacy requirements.

## Applications:
- Critical infrastructure protection
- Industrial IoT security
- Smart grid cybersecurity
- Autonomous system security''',
            'category': 'research',
            'importance': 1,
            'github_url': 'https://github.com/Warrafeeq'
        },
        {
            'title': '6G Network Security Framework',
            'description': 'Security and performance analysis for next-generation wireless networks',
            'content': '''This project investigates the security implications and performance characteristics of 6G wireless communication networks. The research focuses on developing comprehensive security frameworks for the next generation of wireless technology.

## Research Areas:
- **6G Security Architecture**: Design of security protocols for 6G networks
- **Performance Analysis**: Evaluation of security impact on network performance
- **Threat Modeling**: Identification and mitigation of 6G-specific security threats
- **Edge Computing Integration**: Security considerations for 6G-edge computing convergence

## Key Contributions:
- Novel security protocols for 6G networks
- Performance benchmarking of security mechanisms
- Threat analysis and mitigation strategies
- Integration with edge computing security

## Impact:
This research contributes to the foundational security architecture for future 6G networks, ensuring robust protection against emerging cyber threats.''',
            'category': 'research',
            'importance': 2,
            'github_url': 'https://github.com/Warrafeeq'
        },
        {
            'title': 'Edge Computing Optimization Platform',
            'description': 'Computational optimization for edge computing environments',
            'content': '''A comprehensive platform for optimizing computational tasks and data processing at the network edge. This project focuses on enhancing efficiency and responsiveness in distributed edge computing environments.

## Platform Features:
- **Task Scheduling**: Intelligent task distribution across edge nodes
- **Resource Optimization**: Dynamic resource allocation and management
- **Latency Minimization**: Algorithms to reduce processing and communication delays
- **Load Balancing**: Efficient distribution of computational workloads

## Technical Implementation:
- **Python/C++**: Core optimization algorithms
- **Docker**: Containerized edge services
- **Kubernetes**: Orchestration of edge computing resources
- **Machine Learning**: Predictive optimization models

## Use Cases:
- IoT data processing
- Real-time analytics
- Autonomous vehicle computing
- Smart city applications''',
            'category': 'development',
            'importance': 3,
            'github_url': 'https://github.com/Warrafeeq'
        },
        {
            'title': 'Cryptographic Security Tools',
            'description': 'Advanced cryptographic implementations for data protection',
            'content': '''A collection of advanced cryptographic tools and implementations designed to protect data, networks, and systems from malicious attacks. This project focuses on practical cryptographic solutions for modern security challenges.

## Cryptographic Implementations:
- **Symmetric Encryption**: AES, ChaCha20, and other modern ciphers
- **Asymmetric Cryptography**: RSA, ECC, and post-quantum algorithms
- **Hash Functions**: SHA-3, BLAKE2, and specialized hash implementations
- **Digital Signatures**: ECDSA, EdDSA, and quantum-resistant signatures

## Security Features:
- **Side-Channel Resistance**: Protection against timing and power analysis attacks
- **Quantum Resistance**: Implementation of post-quantum cryptographic algorithms
- **Performance Optimization**: Efficient implementations for various platforms
- **Security Analysis**: Comprehensive testing and validation tools

## Applications:
- Secure communication protocols
- Data encryption and protection
- Digital identity verification
- Blockchain and cryptocurrency security''',
            'category': 'development',
            'importance': 4,
            'github_url': 'https://github.com/Warrafeeq'
        },
        {
            'title': 'Critical Infrastructure Protection System',
            'description': 'Cybersecurity solutions for power grids and transportation systems',
            'content': '''A comprehensive cybersecurity framework designed to protect critical infrastructure systems including power grids, transportation networks, and other vital national assets from cyber threats.

## Protection Domains:
- **Power Grid Security**: SCADA system protection and monitoring
- **Transportation Security**: Railway and traffic management system security
- **Water Treatment**: Industrial control system cybersecurity
- **Communication Networks**: Critical communication infrastructure protection

## Security Mechanisms:
- **Intrusion Detection**: Real-time threat monitoring and detection
- **Anomaly Analysis**: Machine learning-based anomaly detection
- **Incident Response**: Automated response to security incidents
- **Forensic Analysis**: Post-incident investigation and analysis tools

## Technical Stack:
- **Python/Java**: Core security applications
- **Machine Learning**: TensorFlow/PyTorch for threat detection
- **Network Security**: Custom IDS/IPS implementations
- **Industrial Protocols**: Modbus, DNP3, IEC 61850 security

## Impact:
This system provides comprehensive protection for critical national infrastructure, ensuring continuity of essential services and protection against sophisticated cyber attacks.''',
            'category': 'research',
            'importance': 5,
            'github_url': 'https://github.com/Warrafeeq'
        },
        {
            'title': 'Agricultural Technology Security',
            'description': 'Cybersecurity solutions for smart agriculture and IoT farming systems',
            'content': '''This project focuses on securing agricultural technology systems, including IoT sensors, automated farming equipment, and precision agriculture platforms against cyber threats.

## Agricultural Security Focus:
- **IoT Sensor Security**: Protection of environmental and crop monitoring sensors
- **Automated Equipment**: Security for tractors, drones, and robotic systems
- **Data Protection**: Securing farm data and agricultural analytics
- **Supply Chain Security**: Protection of agricultural supply chain systems

## Security Solutions:
- **Device Authentication**: Secure authentication for agricultural IoT devices
- **Data Encryption**: Protection of sensitive agricultural data
- **Network Segmentation**: Isolation of critical agricultural systems
- **Threat Intelligence**: Agricultural-specific threat monitoring

## Technologies Used:
- **IoT Security Protocols**: MQTT, CoAP security implementations
- **Blockchain**: Supply chain traceability and security
- **Machine Learning**: Predictive security analytics
- **Edge Computing**: Local processing for agricultural data

## Benefits:
- Protection of agricultural intellectual property
- Ensuring food supply chain security
- Preventing disruption of automated farming systems
- Maintaining farmer privacy and data security''',
            'category': 'research',
            'importance': 6,
            'github_url': 'https://github.com/Warrafeeq'
        }
    ]
    
    for proj in projects_data:
        Project.objects.create(**proj)
        print(f"Added project: {proj['title']}")
    
    print(f"Added {len(projects_data)} GitHub projects")

if __name__ == '__main__':
    print("Adding GitHub projects for Muhammed Rafeeq War...")
    add_github_projects()
    print("GitHub projects added successfully!")
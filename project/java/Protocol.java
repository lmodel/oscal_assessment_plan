package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Information about the protocol used to provide a service.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Protocol  {

  private String uuid;
  private String name;
  private String title;
  private List<PortRange> port-ranges;

}
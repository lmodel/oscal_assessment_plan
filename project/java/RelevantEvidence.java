package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Links this observation to relevant evidence.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RelevantEvidence  {

  private String href;
  private String description;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}